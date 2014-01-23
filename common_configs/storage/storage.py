#-*- coding: utf-8 -*-
"""
Storage settings for static and media files.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import datetime
import time

from django.utils.http import http_date
from configurations import values

from ..services.aws import AWS
from ..utils import merge_items


class SimpleStorage(object):
    """
    Base class for static and media storage settings
    """

    STATIC_URL = "/static/"
    MEDIA_URL = "/media/"


class BaseCompressStorage(SimpleStorage):
    """
    Enables django-compress static files finder
    """

    #: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-STATICFILES_FINDERS
    STATICFILES_FINDERS = values.ListValue([
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
        "compressor.finders.CompressorFinder",
    ])


class LocalCompressStorage(BaseCompressStorage):
    pass


class AWSCompressStorage(AWS, BaseCompressStorage):
    """
    S3 AWS based storage settings configured for use with django_compressor.

    For more info see:

        - https://docs.djangoproject.com/en/dev/ref/settings/#default-file-storage
        - http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_STORAGE
        - https://bitbucket.org/david/django-storages/src/tip/storages/backends/s3boto.py

    """

    #: https://docs.djangoproject.com/en/dev/ref/settings/#default-file-storage
    DEFAULT_FILE_STORAGE = values.Value("common_configs.storage.backends.S3MediaStorage")

    #: https://docs.djangoproject.com/en/dev/ref/settings/#staticfiles-storage
    STATICFILES_STORAGE = values.Value("common_configs.storage.backends.CachedS3StaticStorage")

    #: http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_STORAGE
    COMPRESS_STORAGE = values.Value("common_configs.storage.backends.CachedS3StaticStorage")

    #: S3 bucket name for stored files
    AWS_STORAGE_BUCKET_NAME = values.SecretValue(environ_prefix=None)

    #: Default S3 ACL settings
    AWS_DEFAULT_ACL = values.Value("public-read")

    #: Overwrite files in S3 storage
    AWS_S3_FILE_OVERWRITE = values.BooleanValue(True, environ_prefix=None)

    #: Use secure SSL urls for serving objects from S3
    AWS_S3_SECURE_URLS = values.BooleanValue(True, environ_prefix=None)

    #: Use custom S3 domain
    AWS_S3_CUSTOM_DOMAIN = values.Value("", environ_prefix=None)

    #: CloudFront endpoint url when serving files from CDN
    AWS_CLOUDFRONT_URL = values.Value("", environ_prefix=None)

    #: Generate S3 auth querystring
    AWS_QUERYSTRING_AUTH = values.BooleanValue(False, environ_prefix=None)

    #: Compress uploaded content
    AWS_IS_GZIPPED = values.BooleanValue(False, environ_prefix=None)

    #: Preload S3 metadata
    AWS_PRELOAD_METADATA = values.BooleanValue(True, environ_prefix=None)

    #: Compressable content types (if ``AWS_IS_GZIPPED`` flag is set)
    GZIP_CONTENT_TYPES = values.TupleValue((
        "text/css",
        "application/javascript",
        "application/x-javascript",
    ), environ_prefix="AWS")

    @property
    def AWS_S3_CALLING_FORMAT(self):
        """
        S3 calling format (``SubdomainCallingFormat``).
        """
        from boto.s3.connection import SubdomainCallingFormat
        return SubdomainCallingFormat()

    @property
    def AWS_HEADERS(self):
        """
        Defines far-future expires (2020-12-31) and cache
        control (``public, max-age=604800, must-revalidate``) headers for served files.
        """
        max_age_days = 7
        return {
            "Expires": http_date(
                time.mktime((datetime.datetime(2020, 12, 31)).timetuple())),
            "Cache-Control": "public, max-age=%d, must-revalidate" % (max_age_days * 24 * 60 * 60),
        }

    def get_aws_url(self, path, bucket, calling_format, secure, host="s3.amazonaws.com"):
        protocol = "https://" if secure else "http://"
        root = calling_format.get_bucket_server(host, bucket)
        return "{}{}/{}/".format(protocol, root, path)

    @property
    def STATIC_URL(self):
        """
        Base url for static files
        """
        if self.AWS_CLOUDFRONT_URL:
            return "{}{}/".format(self.AWS_CLOUDFRONT_URL, "static")
        return self.get_aws_url(
            "static", bucket=self.AWS_STORAGE_BUCKET_NAME,
            calling_format=self.AWS_S3_CALLING_FORMAT, secure=self.AWS_S3_SECURE_URLS
        )

    @property
    def MEDIA_URL(self):
        """
        Base url for media files
        """
        if self.AWS_CLOUDFRONT_URL:
            return "{}{}/".format(self.AWS_CLOUDFRONT_URL, "media")
        return self.get_aws_url(
            "media", bucket=self.AWS_STORAGE_BUCKET_NAME,
            calling_format=self.AWS_S3_CALLING_FORMAT, secure=self.AWS_S3_SECURE_URLS
        )

    @property
    def INSTALLED_APPS(self):
        """
        Appends :mod:`collectfast` to list of ``INSTALLED_APPS``.
        """
        return merge_items(super(AWSCompressStorage, self).INSTALLED_APPS, [
            "collectfast"
        ])
