#-*- coding : utf-8 -*-
from .base import *

INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dbLecole',
    }
}
