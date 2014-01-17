#-*- coding: utf-8 -*-

"""
Enable SSL and other security settings for Django and django-secure_ app.

Django-secure install instructions: http://django-secure.rtfd.org/latest/index.html#installation

.. _django-secure: http://django-secure.readthedocs.org/
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from configurations import values


class DjangoSecurity(object):
    ###########################################################
    # Cookie and session settings

    #: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SESSION_COOKIE_SECURE
    SESSION_COOKIE_SECURE = values.BooleanValue(True)

    #: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SESSION_COOKIE_HTTPONLY
    SESSION_COOKIE_HTTPONLY = values.BooleanValue(True)

    #: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-CSRF_COOKIE_SECURE
    CSRF_COOKIE_SECURE = values.BooleanValue(True)

    ###########################################################
    # SSL and content security settings

    #: http://django-secure.rtfd.org/latest/settings.html#secure-frame-deny
    SECURE_FRAME_DENY = values.BooleanValue(True)

    #: http://django-secure.rtfd.org/latest/settings.html#secure-hsts-seconds
    SECURE_HSTS_SECONDS = values.IntegerValue(60 * 60 * 24 * 30)

    #: http://django-secure.rtfd.org/latest/settings.html#secure-hsts-include-subdomains
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)

    #: http://django-secure.rtfd.org/latest/settings.html#secure-content-type-nosniff
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)

    #: http://django-secure.rtfd.org/latest/settings.html#secure-browser-xss-filter
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)

    #: http://django-secure.rtfd.org/latest/settings.html#secure-ssl-redirect
    SECURE_SSL_REDIRECT = values.BooleanValue(True)
