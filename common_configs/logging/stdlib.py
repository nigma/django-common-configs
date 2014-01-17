#-*- coding: utf-8 -*-

"""
Django logging configuration

Defined loggers:

    - <catch all>
    - django
    - django.startup
    - django.request
    - django.db.backends
    - django.commands
    - django.security.DisallowedHost
    - app.* - for project app loggers
    - boto
    - celery
    - requests
    - raven
    - sentry.errors

Defined handlers:

    - mail_admins
    - console
    - console_celery
    - sentry
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import logging

from configurations import values

logging.captureWarnings(True)


class Logging(object):

    #: Default handler
    LOGGING_DEFAULT_HANDLER = values.Value("console")

    #: Default handler for celery
    LOGGING_CELERY_HANDLER = values.Value("console_celery")

    #: Default formatter
    LOGGING_DEFAULT_FORMATTER = values.Value("console")

    #: Add request-id to each log line (requires https://github.com/dabapps/django-log-request-id)
    LOGGING_ADD_REQUEST_ID = values.BooleanValue(True)

    #: Use sentry for error logging
    LOGGING_USE_SENTRY = values.BooleanValue(True)

    def get_request_id_filters(self):
        return ["request_id"] if self.LOGGING_ADD_REQUEST_ID else []

    def get_sentry_handlers(self):
        return ["sentry"] if self.LOGGING_USE_SENTRY else []

    def get_logging_filters(self):
        filters = {
            "require_debug_false": {
                "()": "django.utils.log.RequireDebugFalse"
            }
        }
        if self.LOGGING_ADD_REQUEST_ID:
            filters["request_id"] = {
                "()": "log_request_id.filters.RequestIDFilter"
            }
        return filters

    def get_logging_formatters(self):
        return {
            "standard": {
                "format": "%(asctime)s - %(levelname)-5s [%(name)s:%(lineno)s] %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S"
            },
            "verbose": {
                "format": "%(asctime)s - %(levelname)-5s %(module)s [%(name)s:%(lineno)s] %(process)d %(thread)d %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S"
            },
            "console": {
                "format": "%(asctime)s - %(levelname)-5s [%(name)s:%(lineno)s] %(message)s",
                "datefmt": "%H:%M:%S"
            },
            "heroku": {
                "format": "%(levelname)-5s request_id=%(request_id)s [%(name)s:%(lineno)s] %(message)s"
            },
            "celery": {
                "format": "%(levelname)-5s [%(processName)s:%(name)s:%(lineno)s] [%(task_name)s(%(task_id)s)] %(message)s"
            }
        }

    def get_logging_handlers(self):
        stream = sys.stdout
        handlers = {
            "mail_admins": {
                "level": "ERROR",
                "filters": ["require_debug_false"] + self.get_request_id_filters(),
                "class": "django.utils.log.AdminEmailHandler",
                "include_html": False,
            },
            "console": {
                "level": "DEBUG",
                "filters": self.get_request_id_filters(),
                "class": "logging.StreamHandler",
                "formatter": "heroku",
                "stream": stream
            },
            "console_celery": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "formatter": "celery",
                "stream": stream
            }
        }
        if self.LOGGING_USE_SENTRY:
            handlers["sentry"] = {
                "level": "ERROR",
                "filters": self.get_request_id_filters(),
                "class": "raven.contrib.django.raven_compat.handlers.SentryHandler",
            }
        return handlers

    def get_loggers(self):
        handlers = [self.LOGGING_DEFAULT_HANDLER] + self.get_sentry_handlers()
        return {
            "": {
                "handlers": handlers,
                "level": "WARNING",
            },
            "boto": {
                "handlers": handlers,
                "level": "INFO",
                "propagate": True
            },
            "django": {
                "handlers": handlers,
                "level": "WARNING",
                "propagate": False,
            },
            "django.startup": {
                "handlers": handlers,
                "level": "INFO",
                "propagate": False
            },
            "django.request": {
                "handlers": handlers + ["mail_admins"],
                "level": "ERROR",
                "propagate": False
            },
            "django.db.backends": {
                "level": "ERROR",
                "handlers": handlers,
                "propagate": False
            },
            "django.commands": {
                "handlers": handlers + ["mail_admins"],
                "level": "ERROR",
                "propagate": False
            },
            "django.security.DisallowedHost": {
                "handlers": [],
                "propagate": False,
            },
            "app": {
                "handlers": handlers,
                "level": "DEBUG",
                "propagate": False
            },
            "celery": {
                "handlers": handlers,
                "level": "INFO",
                "propagate": False
            },
            "requests": {
                "handlers": handlers,
                "level": "WARNING",
                "propagate": False
            },
            "raven": {
                "level": "DEBUG",
                "handlers": [self.LOGGING_DEFAULT_HANDLER],
                "propagate": False
            },
            "sentry.errors": {
                "level": "DEBUG",
                "handlers": [self.LOGGING_DEFAULT_HANDLER],
                "propagate": False
            },
        }

    def LOGGING(self):
        """
        Fully configured Django logging
        """
        return {
            "version": 1,
            "disable_existing_loggers": False,
            "root": {
                "level": "WARNING",
                "handlers": [self.LOGGING_DEFAULT_HANDLER] + self.get_sentry_handlers(),
            },
            "formatters": self.get_logging_formatters(),
            "filters": self.get_logging_filters(),
            "handlers": self.get_logging_handlers(),
            "loggers": self.get_loggers()
        }
