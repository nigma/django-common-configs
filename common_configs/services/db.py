#-*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from configurations import values


class Database(object):

    #: Configures Django DATABASES using ``DATABASE_URL`` environment variable
    DATABASES = values.DatabaseURLValue()
