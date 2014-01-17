#-*- coding: utf-8 -*-

"""
Enables `structlog.org <http://www.structlog.org/>`_ logging.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import json

from .stdlib import Logging


class StructLoggingDev(Logging):

    import structlog

    class KeyValueRenderer(structlog.processors.KeyValueRenderer):

        from structlog.processors import _JSONFallbackEncoder

        def __call__(self, _, __, event_dict):
            return ' '.join(k + '=' + json.dumps(v, cls=self._JSONFallbackEncoder)
                            for k, v in self._ordered_items(event_dict))

    @property
    def STRUCTLOG_CONFIGURED(self):
        import structlog

        key_order = ["event"]

        if self.LOGGING_ADD_REQUEST_ID:
            key_order.append("request_id")

        structlog.configure_once(
            processors=[
                structlog.stdlib.filter_by_level,
                structlog.processors.StackInfoRenderer(),
                structlog.processors.format_exc_info,
                self.KeyValueRenderer(key_order=key_order)
            ],
            context_class=dict,
            logger_factory=structlog.stdlib.LoggerFactory(),
            wrapper_class=structlog.stdlib.BoundLogger,
            cache_logger_on_first_use=True
        )
        return True


class StructLoggingProd(Logging):

    @property
    def STRUCTLOG_CONFIGURED(self):
        import structlog

        structlog.configure_once(
            processors=[
                structlog.stdlib.filter_by_level,
                structlog.processors.StackInfoRenderer(),
                structlog.processors.format_exc_info,
                structlog.processors.JSONRenderer
            ],
            context_class=dict,
            logger_factory=structlog.stdlib.LoggerFactory(),
            wrapper_class=structlog.stdlib.BoundLogger,
            cache_logger_on_first_use=True
        )
        return True
