#-*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from configurations import values

from ..apps.celery import CeleryBase
from ..storage.storage import AWSCompressStorage


class PostgresHeroku(object):

    @property
    def DATABASES(self):
        """
        Return a fully configured Django ``DATABASES`` setting.

        Scans environment variables for available postgresql add-on.
        """
        from postgresify import postgresify as get_db_config
        return get_db_config()


class MemcacheHeroku(object):

    @property
    def CACHES(self):
        """
        Return a fully configured Django ``CACHES`` setting.

        Scans environment variables for available memcache add-on.
        Additionally includes Django's LocMemCache backend under ``"locmem"``
        cache name.
        """
        from memcacheify import memcacheify

        caches = memcacheify()
        caches.update({
            "locmem": {
                "BACKEND": "django.core.cache.backends.locmem.LocMemCache"
            },
            "dummy": {
                "BACKEND": "django.core.cache.backends.dummy.DummyCache",
            }
        })
        return caches


class Heroku(MemcacheHeroku, PostgresHeroku, AWSCompressStorage):

    #: SSL proxy header as defined in
    #: `Django settings docs <https://docs.djangoproject.com/en/1.6/ref/settings/#secure-proxy-ssl-header>`_.
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    #: Request Id header
    LOG_REQUEST_ID_HEADER = "HTTP_HEROKU_REQUEST_ID"


class CeleryHerokuBigWig(CeleryBase):

    #: Retrieve broker url settings from BigWig RabbitMQ environment variable
    BROKER_URL = values.SecretValue(environ_name="RABBITMQ_BIGWIG_URL", environ_prefix=None)
    # BROKER_URL = os.environ["RABBITMQ_BIGWIG_RX_URL"] + ";" + os.environ["RABBITMQ_BIGWIG_TX_URL"]


class CeleryHerokuCloudAMQP(CeleryBase):

    #: Retrieve broker url settings from CloudAMQP environment variable
    BROKER_URL = values.SecretValue(environ_name="CLOUDAMQP_URL", environ_prefix=None)
