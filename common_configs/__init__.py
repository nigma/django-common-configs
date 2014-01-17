#-*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import os

__version__ = "0.1.0.dev1"

undefined = object()


def get_env_setting(setting, default=undefined):
    """
    Get the environment setting or raise exception

    :rtype: str
    """

    try:
        return os.environ[setting]
    except KeyError:
        if default is not undefined:
            return default
        error_msg = "Set the %s env variable" % setting
        from django.core.exceptions import ImproperlyConfigured
        raise ImproperlyConfigured(error_msg)
