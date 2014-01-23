#-*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from ..utils import merge_items


class DjangoAuth(object):

    @property
    def INSTALLED_APPS(self):
        """
        Appends :mod:`django.contrib.auth` to list of ``INSTALLED_APPS``.
        """
        return merge_items(super(DjangoAuth, self).INSTALLED_APPS, [
            "django.contrib.auth",
            "django.contrib.sessions",
        ])


    @property
    def MIDDLEWARE_CLASSES(self):
        """
        Appends :class:`django.contrib.sessions.middleware.SessionMiddleware`
        and :class:`django.contrib.auth.middleware.AuthenticationMiddleware`
        to list of ``MIDDLEWARE_CLASSES``.
        """
        return merge_items(super(DjangoAuth, self).MIDDLEWARE_CLASSES, [
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
        ])

    @property
    def TEMPLATE_CONTEXT_PROCESSORS(self):
        """
        Appends auth context processors to list
        of ``TEMPLATE_CONTEXT_PROCESSORS``.
        """
        return super(DjangoAuth, self).TEMPLATE_CONTEXT_PROCESSORS + [
            "django.contrib.auth.context_processors.auth",
        ]

    PASSWORD_HASHERS = [
        "django.contrib.auth.hashers.BCryptPasswordHasher",
        "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    ]


class AllAuth(DjangoAuth):

    @property
    def INSTALLED_APPS(self):
        """
        Appends :mod:`allauth`, :mod:`allauth.account`
        and :mod:`allauth.socialaccount` to list of ``INSTALLED_APPS``.
        """
        return merge_items(super(AllAuth, self).INSTALLED_APPS, [
            "allauth",
            "allauth.account",
            "allauth.socialaccount",

            'allauth.socialaccount.providers.dropbox',
            'allauth.socialaccount.providers.facebook',
            'allauth.socialaccount.providers.github',
            'allauth.socialaccount.providers.google',
            'allauth.socialaccount.providers.persona',
            'allauth.socialaccount.providers.twitter',
        ])

    @property
    def TEMPLATE_CONTEXT_PROCESSORS(self):
        """
        Appends allauth context processors to list
        of ``TEMPLATE_CONTEXT_PROCESSORS``.
        """
        return super(AllAuth, self).TEMPLATE_CONTEXT_PROCESSORS + [
            "allauth.account.context_processors.account",
            "allauth.socialaccount.context_processors.socialaccount",
        ]

    ACCOUNT_AUTHENTICATION_METHOD = "email"
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_EMAIL_VERIFICATION = "mandatory"

    ACCOUNT_USERNAME_BLACKLIST = [
       'www', 'ns1', 'ns2', 'ns3', 'ns4', 'ns5', 'dns',
       'http', 'https', 'news', 'nntp', 'ftp', 'sftp', 'file',
       'mail', 'imap', 'pop3', 'smtp', 'ssh', 'tel',
       'admin', 'registration', 'register', 'about', 'help', 'support',
       'staff', 'root', 'feed', 'blog',
       'noreply', 'media', 'static',
   ]

    AUTHENTICATION_BACKENDS = [
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
    ]
