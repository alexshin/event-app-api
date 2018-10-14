from django.core.management.base import BaseCommand
from ...settings import EVENTBRITE_OAUTH_TOKEN, EVENTBRITE_PROVIDER_ID
from ...services import EventbriteProviderService


class Command(BaseCommand):
    help = 'Grabs events data from Eventbrite and populates DB'

    def add_arguments(self, parser):
        parser.add_argument(
            '-c',
            '--count',
            action='store',
            default=150,
            help='Count of events to be imported from eventbrite'
        )

    def __init__(self):
        super().__init__()

        self.update_service = EventbriteProviderService(provider_id=EVENTBRITE_PROVIDER_ID,
                                                        oauth_token=EVENTBRITE_OAUTH_TOKEN)

    def handle(self, *args, **options):
        self.stdout.write('Start grab data')

        writer = self.stdout.write
        self.update_service.process_events(count=options['count'],
                                           processed_event_callback=lambda x: writer(f'[*] #{x.id} {x.name}'))

        self.stdout.write('Successfully imported!')

