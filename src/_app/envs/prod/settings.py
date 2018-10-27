from os import getenv
from ..shared import *


DEBUG = False

BASE_URL = getenv('APP_BASE_URL', 'http://example.com')

ALLOWED_HOSTS = list(str(getenv('APP_ALLOWED_HOSTS', '127.0.0.1')).split(','))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('APP_SECRET_KEY', 'something difficult to brute force')

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',  # This app uses postgres-json fields, it works only with PGSql
        'NAME':     getenv('POSTGRES_DB', 'app'),
        'USER':     getenv('POSTGRES_USER', 'localroot'),
        'PASSWORD': getenv('POSTGRES_PASSWORD', 'localrootpass'),
        'HOST':     getenv('POSTGRES_HOST', 'postgres'),
        'PORT':     getenv('POSTGRES_PORT', '5432'),
    }
}

# Caches
REDIS_HOST = getenv('REDIS_HOST', 'redis')
REDIS_PORT = getenv('REDIS_PORT', '6379')

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [
                (REDIS_HOST, REDIS_PORT)
            ],
        },
    },
}