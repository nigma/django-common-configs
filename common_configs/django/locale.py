#-*- coding: utf-8 -*-

"""
Django locale, languages and translations
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from configurations import values

gettext_noop = lambda s: s


class Locale(object):

    #: Default timezone
    #:
    #: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
    TIME_ZONE = values.Value("UTC")

    #: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
    LANGUAGE_CODE = values.Value("en-us")

    #: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
    USE_I18N = values.BooleanValue(True)

    #: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
    USE_L10N = values.BooleanValue(True)

    #: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
    USE_TZ = True
