#-*- coding: utf-8 -*-

"""
Sentry/Raven configs
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from configurations import values


class RavenDSNValue(values.SecretValue):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("environ_prefix", None)
        kwargs.setdefault("environ_name", "SENTRY_DSN")
        super(RavenDSNValue, self).__init__(*args, **kwargs)

    def to_python(self, value):
        return {
            "dsn": super(RavenDSNValue, self).to_python(value)
        }


class Raven(object):

    #: Reads Raven connection settings from ``SENTRY_DSN`` environment variable
    RAVEN_CONFIG = RavenDSNValue()

    @property
    def MIDDLEWARE_CLASSES(self):
        """
        Appends :class:`raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware`
        to list of ``MIDDLEWARE_CLASSES``.
        """
        return super(Raven, self).MIDDLEWARE_CLASSES + [
            "raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware"
        ]

    @property
    def INSTALLED_APPS(self):
        """
        Appends :mod:`raven.contrib.django.raven_compat`
        to list of ``INSTALLED_APPS``.
        """
        return super(Raven, self).INSTALLED_APPS + [
            "raven.contrib.django.raven_compat",
        ]
