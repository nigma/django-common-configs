.. _paas:

======================
PaaS Platform settings
======================

Heroku
======

.. automodule:: common_configs.paas.heroku

PostgresHeroku
--------------

.. autoclass:: PostgresHeroku
   :members:

.. code-block:: bash

    heroku addons:add heroku-postgresql
    heroku addons:add pgbackups:auto-month

MemcacheHeroku
--------------

.. autoclass:: MemcacheHeroku
   :members:

.. code-block:: bash

    heroku addons:add memcachier


CeleryHerokuBigWig
------------------

Uses AMQP broker settings for `RabbitMQ Bigwig add-on <https://addons.heroku.com/rabbitmq-bigwig>`_.

.. autoclass:: CeleryHerokuBigWig
   :members:
   :show-inheritance:


.. code-block:: bash

    heroku addons:add rabbitmq-bigwig


CeleryHerokuCloudAMQP
---------------------

Uses AMQP broker settings for `CloudAMQP add-on <https://addons.heroku.com/cloudamqp>`_.

.. autoclass:: CeleryHerokuCloudAMQP
   :members:
   :show-inheritance:


.. code-block:: bash

    heroku addons:add cloudamqp


Heroku
------

.. autoclass:: Heroku
   :members:
   :show-inheritance:
