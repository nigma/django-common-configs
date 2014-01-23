#-*- coding: utf-8 -*-

"""
Settings for django-imagekit_ - automated image processing for Django

.. _django-imagekit: https://github.com/matthewwithanm/django-imagekit
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from configurations import values

from ..utils import merge_items


class Imagekit(object):

    #: Use optimistic strategy
    #:
    #: http://django-imagekit.rtfd.org/latest/configuration.html#django.conf.settings.IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY
    IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY = values.Value("imagekit.cachefiles.strategies.Optimistic", environ_prefix=None)

    #: Define naming strategy
    #:
    #: http://django-imagekit.rtfd.org/latest/configuration.html#django.conf.settings.IMAGEKIT_SPEC_CACHEFILE_NAMER
    IMAGEKIT_SPEC_CACHEFILE_NAMER = values.Value("imagekit.cachefiles.namers.source_name_dot_hash", environ_prefix=None)

    @property
    def INSTALLED_APPS(self):
        """
        Appends :mod:`imagekit` to list of ``INSTALLED_APPS``.
        """
        return merge_items(super(Imagekit, self).INSTALLED_APPS, [
            "imagekit",
        ])
