#-*- coding: utf-8 -*-
from .base import *

with open('/etc/secretkey.txt') as f:
    SECRET_KEY = f.read().strip()

DEBUG = False

ALLOWED_HOSTS = ['.lecole.com.ar']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbLecole',
        'USER': 'root',
        'PASSWORD': 'mirage2520'
    }
}

