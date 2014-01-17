#-*- coding: utf-8 -*-

"""
Cache config
"""

from __future__ import absolute_import, division, print_function, unicode_literals


class CacheDev(object):
    """
    Defines list of caches for development purposes:

        - default: ``DummyCache``
        - locmem: ``LocMemCache``
        - dummy: ``DummyCache``
    """

    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        },
        "locmem": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache"
        },
        "dummy": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        }
    }
