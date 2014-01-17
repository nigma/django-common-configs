============
Installation
============

Add ``django-common-configs=<version>`` to your ``requirements.txt`` file or install
it directly from the command line by invoking::

    $ pip install django-common-configs

or::

    $ easy_install django-common-configs


Additional requirements can be easily installed by specifying list of modules
that are going to be used. For example::

    django-common-configs[security,compress,forms,imagekit,pusher,sentry,storage,structlog,twilio,heroku]==0.1.0

See :ref:`dependencies` for list of optional requirements for each module.

.. note::

    Please note that this package is under development and it
    is recommended to specify an exact package version number
    in your requirements.txt file.
