from os import getenv
from ..shared import *

DEBUG = False
ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b=c(untxoz5s!9sudc9u!)b%(w=029(0d2pzodl04m(3x35e=l'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':     getenv('DJANGO_TEST_DB_NAME', 'app'),
        'USER':     getenv('DJANGO_TEST_DB_USER', 'localroot'),
        'PASSWORD': getenv('DJANGO_TEST_DB_PASS', 'localrootpass'),
        'HOST':     getenv('DJANGO_TEST_DB_HOST', '127.0.0.1'),
        'PORT':     getenv('DJANGO_TEST_DB_PORT', '5432'),
    }
}

CORS_ORIGIN_ALLOW_ALL = True
