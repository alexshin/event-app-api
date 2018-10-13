from django.apps import AppConfig
from django.conf import settings


class EventbriteProviderConfig(AppConfig):
    name = 'event.providers.eventbrite_provider'

    def ready(self):
        from .settings import EVENTBRITE_OAUTH_TOKEN
        if settings.ENVIRONMENT == 'prod':
            assert EVENTBRITE_OAUTH_TOKEN is not None, \
                "You must setup EVENTBRITE_OAUTH_TOKEN via django-settings or environment variable"
