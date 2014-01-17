#-*- coding: utf-8 -*-

"""
Configure push notification credentials for Apple Push Notification Service (APNS)
Production/Enterprise and Google Cloud Messaging for Android (GCM)
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from configurations import values


class APNS(object):

    #: Production server
    APNS_PRODUCTION_SERVER = values.Value("push_production", environ_name="APNS_PRODUCTION_SERVER", environ_prefix=None)

    #: Production feedback server
    APNS_PRODUCTION_FEEDBACK_SERVER = values.Value("feedback_production", environ_name="APNS_PRODUCTION_FEEDBACK_SERVER", environ_prefix=None)

    #: Production certificate file (when cert file is stored in file system)
    APNS_PRODUCTION_CERT_FILE = values.Value(None, environ_name="APNS_PRODUCTION_CERT_FILE", environ_prefix=None)

    #: Production certificate string (when cert is stored as env variable)
    APNS_PRODUCTION_CERT_STRING = values.Value(None, environ_name="APNS_PRODUCTION_CERT_STRING", environ_prefix=None)

    #: Production certificate password
    APNS_PRODUCTION_CERT_PASS = values.Value(None, environ_name="APNS_PRODUCTION_CERT_PASS", environ_prefix=None)

    #: Enterprise server
    APNS_ENTERPRISE_SERVER = values.Value("push_production", environ_name="APNS_ENTERPRISE_SERVER", environ_prefix=None)

    #: Enterprise feedback server
    APNS_ENTERPRISE_FEEDBACK_SERVER = values.Value("feedback_production", environ_name="APNS_ENTERPRISE_FEEDBACK_SERVER", environ_prefix=None)

    #: Enterprise certificate file (when cert file is stored in file system)
    APNS_ENTERPRISE_CERT_FILE = values.Value(None, environ_name="APNS_ENTERPRISE_CERT_FILE", environ_prefix=None)

    #: Enterprise certificate string (when cert is stored as env variable)
    APNS_ENTERPRISE_CERT_STRING = values.Value(None, environ_name="APNS_ENTERPRISE_CERT_STRING", environ_prefix=None)

    #: Enterprise certificate password
    APNS_ENTERPRISE_CERT_PASS = values.Value(None, environ_name="APNS_ENTERPRISE_CERT_PASS", environ_prefix=None)

    @property
    def APNS_CONFIGS(self):
        """
        Dictionary of production and enterprise settings::

            {
                "production": {
                    "server": ..,
                    "feedback_server": ..,
                    "cert_file": ..,
                    "cert_string": ..,
                    "cert_pass": ..,
                },
                "enterprise": ..
            }

        :rtype: dict
        """
        return {
            "production": {
                "server": self.APNS_PRODUCTION_SERVER,
                "feedback_server": self.APNS_PRODUCTION_FEEDBACK_SERVER,
                "cert_file": self.APNS_PRODUCTION_CERT_FILE,
                "cert_string": self.APNS_PRODUCTION_CERT_STRING,
                "cert_pass": self.APNS_PRODUCTION_CERT_PASS,
            },
            "enterprise": {
                "server": self.APNS_ENTERPRISE_SERVER,
                "feedback_server": self.APNS_ENTERPRISE_FEEDBACK_SERVER,
                "cert_file": self.APNS_ENTERPRISE_CERT_FILE,
                "cert_string": self.APNS_ENTERPRISE_CERT_STRING,
                "cert_pass": self.APNS_ENTERPRISE_CERT_PASS,
            }
        }


class GCM(object):

    #: API key
    GCM_API_KEY = values.SecretValue(environ_prefix=None)

    #: Dry run flag
    GCM_DRY_RUN = values.BooleanValue(False, environ_prefix=None)
