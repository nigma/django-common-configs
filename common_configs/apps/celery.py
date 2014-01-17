#-*- coding: utf-8 -*-

"""
Celery_ settings for dev and base production environment.

.. _Celery: http://www.celeryproject.org/

See http://docs.celeryproject.org/en/latest/configuration.html for settings description.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import datetime

from configurations import values


class CeleryBase(object):

    #: Timezone
    CELERY_TIMEZONE = "UTC"

    #: The number of concurrent worker processes/threads/green threads executing tasks.
    CELERYD_CONCURRENCY = values.IntegerValue(12, environ_prefix=None)

    #: How many messages to prefetch at a time multiplied by the number of concurrent processes.
    CELERYD_PREFETCH_MULTIPLIER = values.IntegerValue(1, environ_prefix=None)

    #: The backend used to store task results (tombstones). Disabled by default.
    CELERY_RESULT_BACKEND = values.Value(None)

    #: Result serialization format.
    CELERY_RESULT_SERIALIZER = values.Value("json")

    ##: A whitelist of content-types/serializers to allow.
    #CELERY_ACCEPT_CONTENT = ['json']

    ##: A string identifying the default serialization method to use
    #CELERY_TASK_SERIALIZER = "pickle"

    #: Default broker URL.
    BROKER_URL = values.Value(None, environ_prefix="CELERY")

    #: The maximum number of connections that can be open in the connection pool.
    BROKER_POOL_LIMIT = values.IntegerValue(3, environ_prefix="CELERY")

    #: Whether to store the task return values or not (tombstones).
    CELERY_IGNORE_RESULT = values.BooleanValue(True)

    #: Default compression used for task messages.
    CELERY_MESSAGE_COMPRESSION = "gzip"

    #: Time (in seconds, or a timedelta object) for when after stored task tombstones will be deleted.
    CELERY_TASK_RESULT_EXPIRES = datetime.timedelta(minutes=30).total_seconds()

    ##: This setting defines what happens when a task part of a chord raises an exception:
    ##: If propagate is True the chord callback will change state to FAILURE with the exception
    ##:  value set to a ChordError instance containing information about the error and the task that failed.
    ##: If propagate is False the exception value will instead be forwarded to the chord callback.
    #CELERY_CHORD_PROPAGATES = True  # default True

    # CELERY_TRACK_STARTED = True  # Disable this report after testing

    #: Late ack means the task messages will be acknowledged after the task has been executed,
    #: not just before, which is the default behavior.
    #: https://docs.celeryproject.org/en/latest/faq.html#faq-acks-late-vs-retry
    CELERY_ACKS_LATE = True

    #: Maximum number of tasks a pool worker process can execute before it’s replaced with a new one. Default is no limit.
    CELERYD_MAX_TASKS_PER_CHILD = values.IntegerValue(200)

    #: Task hard time limit in seconds. The worker processing the task will be killed and replaced with a new one when this is exceeded.
    CELERYD_TASK_TIME_LIMIT = values.IntegerValue(90)

    #: Errors occurring during task execution will be sent to ADMINS by email.
    CELERY_SEND_TASK_ERROR_EMAILS = values.BooleanValue(True)

    CELERYD_HIJACK_ROOT_LOGGER = False

    CELERYBEAT_SCHEDULE = {
        # "hourly-entry-name": {
        #     "task": "tasks.task_name",
        #     "schedule": datetime.timedelta(minutes=60)
        # }
    }


class CeleryDev(CeleryBase):

    #: Run queued tasks immediately
    CELERY_ALWAYS_EAGER = True

    #: Propagate exceptions to front-end debugger
    CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
