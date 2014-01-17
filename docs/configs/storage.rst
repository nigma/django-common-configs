.. _storage:

=============================
Storage settings and backends
=============================

Storage settings
================

.. automodule:: common_configs.storage.storage

SimpleStorage
-------------

.. autoclass:: SimpleStorage
  :members:
  :show-inheritance:


BaseCompressStorage
-------------------

.. autoclass:: BaseCompressStorage
  :members:
  :show-inheritance:

AWSCompressStorage
------------------

.. autoclass:: AWSCompressStorage
  :members:
  :show-inheritance:

LocalCompressStorage
--------------------

.. autoclass:: LocalCompressStorage
  :members:
  :show-inheritance:

Storage backends
================

.. automodule:: common_configs.storage.backends

Django config
-------------

Remember to configure and include :ref:`aws` config in your settings
as well enable user environment variables in the
`Slug compilation <https://devcenter.heroku.com/articles/slug-compiler>`_ build
phase, so the storage backend is able to connect to S3 when executing
``collectstatic`` and ``compress`` commands:

  .. code-block: shell

    heroku labs:enable user-env-compile

.. note::

    `Django on Heroku: installing NodeJS and Less for static assets
    compilation <http://en.ig.ma/notebook/2012/django-heroku-nodejs-and-less-compiling-assets>`_
    and `Django and Heroku Cookbook <https://github.com/nigma/heroku-django-cookbook>`_
    provides more information and build scripts for automatic static files
    compression during deployment.

Available storage backends
--------------------------

S3 Static and Media storage
+++++++++++++++++++++++++++

.. autoclass:: common_configs.storage.backends.S3StaticStorage

.. autoclass:: common_configs.storage.backends.S3MediaStorage

.. autoclass:: common_configs.storage.backends.NonDeletingS3MediaStorage


Django Compressor-compatible storage
++++++++++++++++++++++++++++++++++++

.. autoclass:: common_configs.storage.backends.CachedS3BotoStorage

.. autoclass:: common_configs.storage.backends.CachedS3StaticStorage
