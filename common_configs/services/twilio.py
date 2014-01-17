#-*- coding: utf-8 -*-

"""
Twilio account config
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from configurations import values


class Twilio(object):

    #: Account SID
    TWILIO_ACCOUNT_SID = values.SecretValue(environ_prefix=None)

    #: Auth token
    TWILIO_AUTH_TOKEN = values.SecretValue(environ_prefix=None)

    #: Default phone number
    TWILIO_PHONE_NUMBER = values.SecretValue(environ_prefix=None)

    TWILIO_SKIP_SIGNATURE_VALIDATION = values.BooleanValue(False, environ_prefix=None)
    TWILIO_CALLBACK_DOMAIN = values.Value("", environ_prefix=None)
    TWILIO_CALLBACK_USE_HTTPS = values.BooleanValue(True, environ_prefix=None)
