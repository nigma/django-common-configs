#-*- coding: utf-8 -*-

"""
Settings for django-crispy-forms_ - the best way to have DRY Django forms

.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from configurations.values import BooleanValue, Value


class CrispyForms(object):

    #: Template pack
    CRISPY_TEMPLATE_PACK = Value("bootstrap3")

    #: Don't suppress errors unless explicitly set
    CRISPY_FAIL_SILENTLY = BooleanValue(False)
