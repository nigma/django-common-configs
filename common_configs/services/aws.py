#-*- coding: utf-8 -*-

"""
Reads common AWS settings like ``AWS_ACCESS_KEY_ID`` and ``AWS_SECRET_ACCESS_KEY``
from environment.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from configurations import values


class AWS(object):

    #: AWS access key id retrieved from ``AWS_ACCESS_KEY_ID`` environment setting
    AWS_ACCESS_KEY_ID = values.SecretValue(environ_prefix=None)

    #: AWS secret key retrieved from ``AWS_SECRET_ACCESS_KEY`` environment setting
    AWS_SECRET_ACCESS_KEY = values.SecretValue(environ_prefix=None)
