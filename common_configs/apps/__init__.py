#-*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from .celery import CeleryBase, CeleryDev
from .compress import CompressBase, CompressDev, CompressProd
from .forms import CrispyForms
from .imagekit import Imagekit
from .auth import DjangoAuth, AllAuth