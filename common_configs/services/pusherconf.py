#-*- coding: utf-8 -*-

"""
Pusher service config
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from configurations import values
from django.utils.encoding import force_bytes


class Pusher(object):

    #: Pusher Socket URL
    PUSHER_SOCKET_URL = values.Value(environ_prefix=None)

    #: Pusher endpoint URL
    PUSHER_URL = values.Value(environ_prefix=None)

    def get_pusher_options(self):
        import pusher
        return pusher.url2options(self.PUSHER_URL)

    @property
    def PUSHER_APP_ID(self):
        """Pusher app id from PUSHER_URL"""
        return force_bytes(self.get_pusher_options()["app_id"])

    @property
    def PUSHER_KEY(self):
        """Pusher key from PUSHER_URL"""
        return force_bytes(self.get_pusher_options()["key"])

    @property
    def PUSHER_SECRET(self):
        """Pusher secret from PUSHER_URL"""
        return force_bytes(self.get_pusher_options()["secret"])

    @property
    def PUSHER_HOST(self):
        """Pusher host from PUSHER_URL"""
        return force_bytes(self.get_pusher_options()["host"])
