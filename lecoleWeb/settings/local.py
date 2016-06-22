#-*- coding : utf-8 -*-
from .base import *

INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',
    'django.contrib.sitemaps'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dbLecole',
    }
}
