#-*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from configurations import Configuration as _Configuration, values


class Configuration(_Configuration):

    @property
    def INSTALLED_APPS(self):
        return []

    @property
    def MIDDLEWARE_CLASSES(self):
        return []

    @property
    def TEMPLATE_CONTEXT_PROCESSORS(self):
        return []
