#-*- coding: utf-8 -*-

"""
Retrieves email backend config from environment variables
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from configurations import values


class Mailgun(object):
    """
    Use Mailgun as email backend
    """

    #: Mailgun api key for using the REST API
    MAILGUN_API_KEY = values.SecretValue(environ_name="MAILGUN_API_KEY", environ_prefix=None)

    #: Mailgun SMTP server host
    MAILGUN_SMTP_SERVER = values.Value("smtp.mailgun.org", environ_name="MAILGUN_SMTP_SERVER", environ_prefix=None)

    #: Mailgun SMTP server login
    MAILGUN_SMTP_LOGIN = values.SecretValue(environ_name="MAILGUN_SMTP_LOGIN", environ_prefix=None)

    #: Mailgun SMTP server password
    MAILGUN_SMTP_PASSWORD = values.SecretValue(environ_name="MAILGUN_SMTP_PASSWORD", environ_prefix=None)

    #: Mailgun SMTP server port
    MAILGUN_SMTP_PORT = values.IntegerValue(587, environ_name="MAILGUN_SMTP_PORT", environ_prefix=None)

    #: Email host for sending mail
    EMAIL_HOST = MAILGUN_SMTP_SERVER

    #: Email server username
    EMAIL_HOST_USER = MAILGUN_SMTP_LOGIN

    #: Email server password
    EMAIL_HOST_PASSWORD = MAILGUN_SMTP_PASSWORD

    #: Email server SMTP port
    EMAIL_PORT = MAILGUN_SMTP_PORT

    #: Email server TLS secure connection
    EMAIL_USE_TLS = True

    #: Email backend
    EMAIL_BACKEND = values.Value("django.core.mail.backends.smtp.EmailBackend")


class Sendgrid(object):
    """
    Use Sendgrid as email backend
    """

    #: Sendgrid SMTP server host
    SENDGRID_SMTP_SERVER = values.Value("smtp.sendgrid.net", environ_name="SENDGRID_SMTP_SERVER", environ_prefix=None)

    #: Sendgrid SMTP server login
    SENDGRID_USERNAME = values.SecretValue(environ_name="SENDGRID_USERNAME", environ_prefix=None)

    #: Sendgrid SMTP server password
    SENDGRID_PASSWORD = values.SecretValue(environ_name="SENDGRID_PASSWORD", environ_prefix=None)

    #: Sendgrid SMTP server port
    SENDGRID_SMTP_PORT = values.IntegerValue(587, environ_name="SENDGRID_SMTP_PORT", environ_prefix=None)

    #: Email host for sending mail
    EMAIL_HOST = SENDGRID_SMTP_SERVER

    #: Email server username
    EMAIL_HOST_USER = SENDGRID_USERNAME

    #: Email server password
    EMAIL_HOST_PASSWORD = SENDGRID_PASSWORD

    #: Email server SMTP port
    EMAIL_PORT = SENDGRID_SMTP_PORT

    #: Email server TLS secure connection
    EMAIL_USE_TLS = True

    #: Email backend
    EMAIL_BACKEND = values.Value("django.core.mail.backends.smtp.EmailBackend")
