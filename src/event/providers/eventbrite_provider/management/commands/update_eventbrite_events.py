from django.core.management.base import BaseCommand, CommandError
from eventbrite import Eventbrite
from ...settings import EVENTBRITE_OAUTH_TOKEN


class Command(BaseCommand):
    help = 'Grabs events data from Eventbrite and populates DB'

    def __init__(self):
        super().__init__()

        self.api = self._get_api_client()

    def handle(self, *args, **options):
        self.stdout.write('Start grab data')

        events = self.api.event_search(expand='organizer,ticket_availability,category')
        n = 1

    @staticmethod
    def _get_api_client():
        return Eventbrite(EVENTBRITE_OAUTH_TOKEN)
