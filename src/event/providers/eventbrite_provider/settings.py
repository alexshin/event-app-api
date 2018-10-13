from os import getenv
from django.conf import settings


EVENTBRITE_OAUTH_TOKEN = getattr(settings, 'EVENTBRITE_OAUTH_TOKEN', getenv('EVENTBRITE_OAUTH_TOKEN'))

EVENTBRITE_PROVIDER_ID = getattr(settings, 'EVENTBRITE_OAUTH_TOKEN', 1)
