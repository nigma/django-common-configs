.. _services:

======================
Common Services mixins
======================

.. _aws:

Amazon AWS settings
===================

.. automodule:: common_configs.services.aws

AWS
---

.. autoclass:: AWS
   :members:


Use ``heroku config`` command to define the values:

  .. code-block:: bash

    heroku config:add AWS_ACCESS_KEY_ID=<key id>
    heroku config:add AWS_SECRET_ACCESS_KEY=<secret key>


Cache settings
==============

.. automodule:: common_configs.services.cache

CacheDev
--------

.. autoclass:: CacheDev
   :members:


Database settings
=================

.. automodule:: common_configs.services.db

Database
--------

.. autoclass:: Database
   :members:


Email settings
==============

.. automodule:: common_configs.services.mail

Mailgun
-------

.. autoclass:: Mailgun
   :members:

Sendgrid
--------

.. autoclass:: Sendgrid
   :members:


Push notification settings
==========================

.. automodule:: common_configs.services.push

APNS
--------

.. autoclass:: APNS
   :members:

GCM
-------

.. autoclass:: GCM
   :members:


Pusher settings
===============

.. automodule:: common_configs.services.pusherconf

Pusher
------

.. autoclass:: Pusher
   :members:


Sentry settings
===============

.. automodule:: common_configs.services.sentry

Raven
-----

.. autoclass:: Raven
   :members:


Twilio settings
===============

.. automodule:: common_configs.services.twilio

Twilio
------

.. autoclass:: Twilio
   :members:
