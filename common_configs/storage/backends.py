#-*- coding: utf-8 -*-

"""
Defines S3 bucket subdirectory storage for static and media files
that utilize `django-storages <http://django-storages.readthedocs.org/en/latest/>`_
and provides storage backends that are compatible with
`Django Compressor <http://django_compressor.readthedocs.org/en/latest/>`_.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import logging

from django.core.files.storage import get_storage_class

from boto.utils import parse_ts
from storages.backends.s3boto import S3BotoStorage

logger = logging.getLogger("app.util.storage")


class S3StaticStorage(S3BotoStorage):
    """
    Subclasses :class:`storages.backends.s3boto.S3BotoStorage` and
    sets base location for files to ``/static``.
    """
    def __init__(self, *args, **kwargs):
        kwargs["location"] = "static"
        kwargs.setdefault("preload_metadata", True)
        super(S3StaticStorage, self).__init__(*args, **kwargs)


class S3MediaStorage(S3BotoStorage):
    """
    Subclasses :class:`storages.backends.s3boto.S3BotoStorage` and
    sets base location for files to ``/media``.
    """
    def __init__(self, *args, **kwargs):
        kwargs["location"] = "media"
        super(S3MediaStorage, self).__init__(*args, **kwargs)


class NonDeletingS3MediaStorage(S3MediaStorage):

    def delete(self, name):
        logger.debug("NOOP file delete: %s", name)
        return


class CachedS3BotoStorage(S3BotoStorage):
    """
    S3 storage backend that saves the files both remotely and locally.

    See http://django_compressor.readthedocs.org/en/latest/remote-storages/
    """
    def __init__(self, *args, **kwargs):
        super(CachedS3BotoStorage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class(
            "compressor.storage.CompressorFileStorage")()

    def save(self, name, content):
        name = super(CachedS3BotoStorage, self).save(name, content)
        self.local_storage._save(name, content)
        return name

    def modified_time(self, name):
        name = self._normalize_name(self._clean_name(name))
        entry = self.entries.get(name)
        if entry is None:
            entry = self.bucket.get_key(self._encode_name(name))
        # Parse the last_modified string to a local datetime object.
        return parse_ts(entry.last_modified)


class CachedS3StaticStorage(CachedS3BotoStorage):
    """
    Mix of the :class:`S3StaticStorage` and :class:`CachedS3BotoStorage`,
    saves files in ``/static`` subdirectory
    """
    def __init__(self, *args, **kwargs):
        kwargs["location"] = "static"
        super(CachedS3StaticStorage, self).__init__(*args, **kwargs)
