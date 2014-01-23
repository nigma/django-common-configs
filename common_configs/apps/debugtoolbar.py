#-*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from ..utils import merge_items


class DebugToolbar(object):

    @property
    def MIDDLEWARE_CLASSES(self):
        """
        Appends :class:`debug_toolbar.middleware.DebugToolbarMiddleware`
        to list of ``MIDDLEWARE_CLASSES``.
        """
        return merge_items(super(DebugToolbar, self).MIDDLEWARE_CLASSES, [
            "debug_toolbar.middleware.DebugToolbarMiddleware"
        ] if self.DEBUG else [])

    @property
    def INSTALLED_APPS(self):
        """
        Appends :mod:`debug_toolbar` to list of ``INSTALLED_APPS``.
        """
        return merge_items(super(DebugToolbar, self).INSTALLED_APPS, [
            "debug_toolbar"
        ] if self.DEBUG else [])
