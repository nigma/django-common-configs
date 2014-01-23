#-*- coding: utf-8 -*-

"""
Enable SSL and other security settings for Django and django-secure_ app.

Django-secure install instructions: http://django-secure.rtfd.org/latest/index.html#installation

.. _django-secure: http://django-secure.readthedocs.org/
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from configurations import values

from ..utils import merge_items


class DjangoSecurity(object):
    """
    Configures some good defaults for non-SSL sites.

    For SSL-enabled sites use :class:`DjangoSSLSecurity`.
    """

    ###########################################################
    # Cookie and session settings

    #: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SESSION_COOKIE_SECURE
    SESSION_COOKIE_SECURE = values.BooleanValue(False)

    #: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SESSION_COOKIE_HTTPONLY
    SESSION_COOKIE_HTTPONLY = values.BooleanValue(True)

    #: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-CSRF_COOKIE_SECURE
    CSRF_COOKIE_SECURE = values.BooleanValue(False)

    ###########################################################
    # SSL and content security settings

    #: http://django-secure.rtfd.org/latest/settings.html#secure-frame-deny
    SECURE_FRAME_DENY = values.BooleanValue(True)

    #: http://django-secure.rtfd.org/latest/settings.html#secure-content-type-nosniff
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)

    #: http://django-secure.rtfd.org/latest/settings.html#secure-browser-xss-filter
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)

    @property
    def INSTALLED_APPS(self):
        """
        Appends :mod:`djangosecure` to list of ``INSTALLED_APPS``.
        """
        apps = super(DjangoSecurity, self).INSTALLED_APPS
        return merge_items(apps, ["djangosecure"])

    @property
    def MIDDLEWARE_CLASSES(self):
        """
        Appends :mod:`djangosecure` to list of ``INSTALLED_APPS``.
        """
        middleware = super(DjangoSecurity, self).MIDDLEWARE_CLASSES
        return merge_items(middleware, [
            "djangosecure.middleware.SecurityMiddleware",
            "django.middleware.clickjacking.XFrameOptionsMiddleware",
        ])


class DjangoSSLSecurity(DjangoSecurity):
    """
    Adds SSL-related settings to :class:`DjangoSecurity`
    """

    ###########################################################
    # Cookie and session settings

    #: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SESSION_COOKIE_SECURE
    SESSION_COOKIE_SECURE = values.BooleanValue(True)

    #: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-CSRF_COOKIE_SECURE
    CSRF_COOKIE_SECURE = values.BooleanValue(True)

    ###########################################################
    # SSL and content security settings

    #: http://django-secure.rtfd.org/latest/settings.html#secure-hsts-seconds
    SECURE_HSTS_SECONDS = values.IntegerValue(60 * 60 * 24 * 30)

    #: http://django-secure.rtfd.org/latest/settings.html#secure-hsts-include-subdomains
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)

    #: http://django-secure.rtfd.org/latest/settings.html#secure-ssl-redirect
    SECURE_SSL_REDIRECT = values.BooleanValue(True)


class MozillaCSP(object):
    """
    Mozilla Content Security Policy that defines several
    default policies for scripts and static assets.

    You most probably will want to adjust it according to static storage and CDN usage
    to white-list all static files sources.
    """

    def csp_get_static_url(self):
        if self.STATIC_URL and self.STATIC_URL.startswith("http"):
            import urlparse
            data = urlparse.urlsplit(self.STATIC_URL)
            if data.netloc:
                return urlparse.urlunsplit((data.scheme, data.netloc, "", "", ""))
        return ""

    #: http://django-csp.readthedocs.org/en/latest/configuration.html#policy-settings
    def CSP_DEFAULT_SRC(self):
        """
        By default allows ``"'self'", STATIC_URL host``
        """
        return ("'self'", self.csp_get_static_url())

    #: http://django-csp.readthedocs.org/en/latest/configuration.html#policy-settings
    def CSP_IMG_SRC(self):
        """
        By default allows ``"*", "data:"``
        """
        return ("*", "data:")

    #: http://django-csp.readthedocs.org/en/latest/configuration.html#policy-settings
    def CSP_SCRIPT_SRC(self):
        """
        By default allows
        ``"'self'", "https://ajax.googleapis.com", "https://code.jquery.com", "https://netdna.bootstrapcdn.com", "'unsafe-inline'", STATIC_URL host``
        """
        return ("'self'", "https://ajax.googleapis.com", "https://code.jquery.com", "https://netdna.bootstrapcdn.com", "'unsafe-inline'", self.csp_get_static_url())

    #: http://django-csp.readthedocs.org/en/latest/configuration.html#policy-settings
    def CSP_FONT_SRC(self):
        """
        By default allows
        ``"'self'", "https://themes.googleusercontent.com", "https://netdna.bootstrapcdn.com", STATIC_URL host``
        """
        return ("'self'", "https://themes.googleusercontent.com", "https://netdna.bootstrapcdn.com", self.csp_get_static_url())

    #: http://django-csp.readthedocs.org/en/latest/configuration.html#policy-settings
    def CSP_STYLE_SRC(self):
        """
        By default allows:
        ``"'self'", "https://fonts.googleapis.com", "https://netdna.bootstrapcdn.com", "'unsafe-inline'", STATIC_URL host``
        """
        return ("'self'", "https://fonts.googleapis.com", "https://netdna.bootstrapcdn.com", "'unsafe-inline'", self.csp_get_static_url())

    CSP_REPORT_ONLY = values.BooleanValue(False)

    @property
    def MIDDLEWARE_CLASSES(self):
        """
        Appends :mod:`djangosecure` to list of ``INSTALLED_APPS``.
        """
        middleware = super(MozillaCSP, self).MIDDLEWARE_CLASSES
        return merge_items(middleware, ["csp.middleware.CSPMiddleware"])
