#-*- coding: utf-8 -*-

"""
Single site config.

Set site id, domain name, default emails and allowed hosts.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from configurations import values


class SingleSite(object):

    #: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
    SITE_ID = values.IntegerValue(1)

    #: Default domain name (for email settings, allowed hosts list and session cookie domain)
    DOMAIN_NAME = values.SecretValue()

    #: Default site name (for email name settings)
    SITE_NAME = values.SecretValue()

    ###########################################################
    # Site emails

    def get_default_from_email(self):
        return "{} <info@{}>".format(self.SITE_NAME, self.DOMAIN_NAME)

    def get_server_email(self):
        return "server@{}".format(self.DOMAIN_NAME)

    def get_email_subject_prefix(self):
        return "[{}] ".format(self.SITE_NAME)

    #: Default: ``info@<domain name>``
    DEFAULT_FROM_EMAIL = values.Value(get_default_from_email)

    #: Default: ``server@<domain name>``
    SERVER_EMAIL = values.Value(get_server_email)

    #: Default: ``[site name]``
    EMAIL_SUBJECT_PREFIX = values.Value(get_email_subject_prefix)

    ###########################################################
    # Allowed hosts and cookie domain

    def get_allowed_hosts(self):
        return [
            self.DOMAIN_NAME,
            "www.{}".format(self.DOMAIN_NAME),
            "api.{}".format(self.DOMAIN_NAME)
        ]

    def get_session_cookie_domain(self):
        return "{}".format(self.DOMAIN_NAME)

    #: Default: ``<domain name>``, ``www.<domain name>``, ``api.<domain name>``
    ALLOWED_HOSTS = values.ListValue(get_allowed_hosts)

    #: Default: ``<domain name>``
    SESSION_COOKIE_DOMAIN = values.Value(get_session_cookie_domain)
