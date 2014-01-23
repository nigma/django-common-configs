=====================
django-common-configs
=====================

.. image:: https://badge.fury.io/py/django-common-configs.png
    :target: http://badge.fury.io/py/django-common-configs

.. image:: https://pypip.in/d/django-common-configs/badge.png
    :target: https://crate.io/packages/django-common-configs?version=latest

Common Configuration settings for Django projects.

Goes in line with `12 factor app <http://12factor.net/config>`_ and popular hosting
platforms like `Heroku <https://www.heroku.com/>`_.

Developed and used at `en.ig.ma software shop <http://en.ig.ma>`_.

Overview
--------

Getting Django and popular apps settings right require time and a bit of experience.

This project provides predefined and verified configs for various aspects
of Django apps, promotes convention over configuration and allows to keep
``settings.py`` file DRY.

It covers security, static files, assets compression, storage, AWS, celery,
Sentry, logging, integration with common services, Heroku and more.

Developed at `en.ig.ma software shop <http://en.ig.ma>`_
and used in multiple `projects <http://en.ig.ma/projects>`_.

Documentation
-------------

The full documentation is at http://django-common-configs.rtfd.org.

Quickstart
----------

Simplify Django project configuration in two easy steps:

Include ``django-common-configs`` and other related packages in your
``requirements.txt`` file.

Install `django-configurations <http://django-configurations.rtfd.org/>`_, add required
common config mixins (they are just plain Python classes) to your ``settings.py``
Configuration classes and override base settings as necessary:


.. code-block:: py

    from configurations import values
    from common_configs.base import BaseConfig

    from common_configs.django import Locale, SingleSite, DjangoSecurity
    from common_configs.apps import CrispyForms, Imagekit, CeleryDev, CompressDev, CompressProd
    from common_configs.logging import StructLoggingDev, StructLoggingProd
    from common_configs.paas.heroku import Heroku, CeleryHerokuBigWig
    from common_configs.services import APNS, GCM, CacheDev, AWS, Mailgun, Sendgrid, Raven, Pusher, Twilio
    from common_configs.storage import LocalCompressStorage, AWSCompressStorage


    class Common(Locale, SingleSite,
                 CrispyForms, Imagekit, APNS, GCM,
                 BaseConfig):

        DEBUG = False
        TEMPLATE_DEBUG = False


    class DevConfig(LocalCompressStorage, CeleryDev, CompressDev, StructLoggingDev, CacheDev,
                    Common):

        DEBUG = True
        TEMPLATE_DEBUG = True
        DATABASES = values.DatabaseURLValue("postgres://...")


    class ProdConfig(AWS, AWSCompressStorage, CeleryHerokuBigWig, CompressProd, StructLoggingProd,
                     Heroku, Mailgun, Raven, Pusher, Twilio,
                     DjangoSecurity,
                     Common):
        pass


.. _dependencies:

Dependencies
------------

``django-common-configs`` depends on ``django-configurations>=0.7`` and optionally on the following packages:

=============== ======================================================================================================
Module              Requirements
=============== ======================================================================================================
security        ``django-secure>=1.0``
compress        ``django_compressor>=1.3``
forms           ``django-crispy-forms>=1.4.0``
imagekit        ``django-imagekit>=3.2``
pusher          ``pusher>=0.8``
sentry          ``raven>=4.0.3``
storage         ``boto>=2.23.0``, ``django-storages>=1.1.8``
logging         ``django-log-request-id>=0.0.3``
structlog       ``structlog>=0.4.1``, ``django-log-request-id>=0.0.3``
twilio          ``twilio``
heroku          ``django-pylibmc-sasl>=0.2.4``, ``django-heroku-memcacheify>=0.4``, ``django-heroku-postgresify>=0.3``
=============== ======================================================================================================

All dependencies can be easily added to your ``requirements.txt`` file by specifying it using pip syntax::

    django-common-configs[security,compress,forms,imagekit,pusher,sentry,storage,structlog,twilio,heroku]==0.1.0


License
-------

`django-common-configs` is released under the BSD license.

Other Resources
---------------

- GitHub repository - https://github.com/nigma/django-common-configs
- PyPi Package site - http://pypi.python.org/pypi/django-common-configs
