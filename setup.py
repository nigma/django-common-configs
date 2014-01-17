#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "0.1.0.dev1"

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open("README.rst").read()
history = open("HISTORY.rst").read().replace(".. :changelog:", "")

setup(
    name="django-common-configs",
    version=version,
    description="""Convention over configuration. Common Configuration settings for Django projects""",
    license="BSD",
    author="Filip Wasilewski",
    author_email="en@ig.ma",
    url="https://github.com/nigma/django-common-configs",
    long_description=readme + "\n\n" + history,
    packages=[
        "common_configs",
    ],
    include_package_data=True,
    install_requires=[
        "django-configurations>=0.7"
    ],
    extras_require={
        "compress": ["django_compressor>=1.3"],
        "forms": ["django-crispy-forms>=1.4.0"],
        "heroku": [
            "django-pylibmc-sasl>=0.2.4",
            "django-heroku-memcacheify>=0.4",
            "django-heroku-postgresify>=0.3"
        ],
        "pusher": ["pusher>=0.8"],
        "sentry": ["raven>=4.0.3"],
        "storage": [
            "boto>=2.23.0",
            "django-storages>=1.1.8"
        ],
        "logging": ["django-log-request-id>=0.0.3"],
        "structlog": ["structlog>=0.4.1", "django-log-request-id>=0.0.3"],
        "security": ["django-secure>=1.0"],
        "twilio": ["twilio"]
    },
    zip_safe=False,
    keywords="django-common-configs",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
