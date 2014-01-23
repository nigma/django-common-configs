#-*- coding: utf-8 -*-

"""
Assets compression settings for django_compressor_

.. _django_compressor: https://github.com/jezdez/django_compressor
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from configurations import values

from ..utils import merge_items


class CompressBase(object):

    #: http://django-compressor.rtfd.org/latest/settings/#django.conf.settings.COMPRESS_ENABLED
    COMPRESS_ENABLED = values.BooleanValue(True)

    #: http://django-compressor.rtfd.org/latest/settings/#django.conf.settings.COMPRESS_PARSER
    COMPRESS_PARSER = values.Value("compressor.parser.default_htmlparser.DefaultHtmlParser")

    #: Predefined list of precompilers. Require installation of 3rd party binaries and packages
    #:
    #: http://django-compressor.rtfd.org/latest/settings/#django.conf.settings.COMPRESS_PRECOMPILERS
    COMPRESS_PRECOMPILERS = [
        ("text/coffeescript", "coffee --compile --stdio"),
        ("text/less", "lessc {infile}"),
        ("text/x-sass", "sass {infile} {outfile}"),
        ("text/x-scss", "sass --scss {infile} {outfile}"),
        ('text/stylus', 'stylus < {infile} > {outfile}'),
    ]

    #: List of css filters (rewrite urls and minify output)
    #:
    #: http://django-compressor.rtfd.org/latest/settings/#django.conf.settings.COMPRESS_CSS_FILTERS
    COMPRESS_CSS_FILTERS = values.ListValue([
        "compressor.filters.css_default.CssAbsoluteFilter",
        "compressor.filters.cssmin.CSSMinFilter"
    ])

    #: List of js filters (minify output)
    #:
    #: http://django-compressor.rtfd.org/latest/settings/#django.conf.settings.COMPRESS_JS_FILTERS
    COMPRESS_JS_FILTERS = values.ListValue([
        "compressor.filters.jsmin.JSMinFilter"
    ])

    #: http://django-compressor.rtfd.org/latest/settings/#django.conf.settings.COMPRESS_OUTPUT_DIR
    COMPRESS_OUTPUT_DIR = values.Value("cache")

    #: http://django-compressor.rtfd.org/latest/settings/#django.conf.settings.COMPRESS_CACHE_BACKEND
    COMPRESS_CACHE_BACKEND = values.Value("locmem")

    @property
    def INSTALLED_APPS(self):
        """
        Appends :mod:`compressor` to list of ``INSTALLED_APPS``.
        """
        return merge_items(super(CompressBase, self).INSTALLED_APPS, [
            "compressor",
        ])


class CompressProd(CompressBase):

    #: Compress assets during deployment
    #:
    #: http://django-compressor.rtfd.org/latest/settings/#django.conf.settings.COMPRESS_OFFLINE
    COMPRESS_OFFLINE = values.BooleanValue(True)


class CompressDev(CompressBase):

    #: Don't minify css in dev
    COMPRESS_CSS_FILTERS = values.Value([
        "compressor.filters.css_default.CssAbsoluteFilter"
    ])

    #: Don't minify concatenated js scripts in dev
    COMPRESS_JS_FILTERS = values.Value([])

    #: Don't cache compiled assets during development
    COMPRESS_CACHE_BACKEND = values.Value("dummy")
