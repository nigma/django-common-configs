#-*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals


def merge_items(base, new_items):
    """
    Merges two lists and eliminates duplicates

    :type base: list
    :type new_items: list
    :rtype: list
    """
    for item in new_items:
        if not item in base:
            base = base + [item]
    return base
