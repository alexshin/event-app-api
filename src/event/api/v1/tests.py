from utils.api_v1_tests import AuthorizedAPITestCase
from event.models import Category, Organizer, Event
from django.utils import timezone
import json


class CategoryViewSetTestCase(AuthorizedAPITestCase):

    list_uri = '/api/v1/categories/'
    retrieve_uri = '/api/v1/categories/{id}/'
    partial_update_uri = '/api/v1/categories/{id}/'

    @staticmethod
    def createCategory(seq_num):
        return Category.objects.create(provider_object_id=f'xxx-{seq_num}', provider=1, name=f'music-{seq_num}')

    def setUp(self):
        super().setUp()
        self.categories = [self.createCategory(i) for i in range(1, 200)]

    def test_list_categories(self):
        resp = self.client.get(self.list_uri)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['count'], 199)
        self.assertEqual(len(resp.data['results']), 100)
        self.assertContains(resp, 'music-1')

    def test_retrieve_category(self):
        c = self.categories[0]
        resp = self.client.get(self.retrieve_uri.format(id=c.pk))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, c.id)
        self.assertContains(resp, c.name)
        self.assertContains(resp, c.provider)

    def test_update_category(self):
        c = self.categories[0]
        resp = self.client.patch(
            self.partial_update_uri.format(id=c.pk),
            data=json.dumps({'name': 'MUSIC-1'}),
            content_type='application/json')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(self.retrieve_uri.format(id=c.pk))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'MUSIC-1')


class OrganizerViewSetTestCase(AuthorizedAPITestCase):

    list_uri = '/api/v1/organizers/'
    retrieve_uri = '/api/v1/organizers/{id}/'
    partial_update_uri = '/api/v1/organizers/{id}/'

    @staticmethod
    def createOrganizer(seq_num):
        return Organizer.objects.create(
            provider_object_id=f'xxx-{seq_num}',
            provider=1,
            name=f'super-organizer-{seq_num}',
            description_plain=f'super-organizer-{seq_num} '*20,
            description_html=f'<b>super-organizer-{seq_num}</b> ' * 20,
            logo_uri='https://google.com',
            uri='https://google.com'
        )

    def setUp(self):
        super().setUp()
        self.organizers = [self.createOrganizer(i) for i in range(1, 200)]

    def test_list_organizers(self):
        resp = self.client.get(self.list_uri)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['count'], 199)
        self.assertEqual(len(resp.data['results']), 100)
        self.assertContains(resp, 'super-organizer')

    def test_retrieve_organizer(self):
        c = self.organizers[0]
        resp = self.client.get(self.retrieve_uri.format(id=c.pk))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, c.id)
        self.assertContains(resp, c.name)
        self.assertContains(resp, c.provider)

    def test_update_organizer(self):
        c = self.organizers[0]
        resp = self.client.patch(
            self.partial_update_uri.format(id=c.pk),
            data=json.dumps({'name': 'not-super-organizer'}),
            content_type='application/json')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(self.retrieve_uri.format(id=c.pk))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'not-super-organizer')


class EventViewSetTestCase(AuthorizedAPITestCase):

    list_uri = '/api/v1/events/'
    retrieve_uri = '/api/v1/events/{id}/'
    partial_update_uri = '/api/v1/events/{id}/'

    @staticmethod
    def createEvent(seq_num):
        return Event.objects.create(
            provider_object_id=f'xxx-{seq_num}',
            provider=1,
            name=f'super-event-{seq_num}',
            description_plain=f'super-event-{seq_num} '*20,
            description_html=f'<b>super-event-{seq_num}</b> ' * 20,
            logo_uri='https://google.com',
            uri='https://google.com',
            category=CategoryViewSetTestCase.createCategory(seq_num),
            organizer=OrganizerViewSetTestCase.createOrganizer(seq_num),
            min_ticket_price=seq_num,
            max_ticket_price=seq_num*100,
            ticket_price_currency='USD',
            start_time=timezone.now(),
            finish_time=timezone.now()
        )

    def setUp(self):
        super().setUp()
        self.events = [self.createEvent(i) for i in range(1, 200)]

    def test_list_events(self):
        resp = self.client.get(self.list_uri)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['count'], 199)
        self.assertEqual(len(resp.data['results']), 100)
        self.assertContains(resp, 'super-event')

    def test_retrieve_event(self):
        c = self.events[-1]
        resp = self.client.get(self.retrieve_uri.format(id=c.pk))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, c.id)
        self.assertContains(resp, c.name)
        self.assertContains(resp, c.provider)

    def test_update_event(self):
        c = self.events[-1]
        resp = self.client.patch(
            self.partial_update_uri.format(id=c.pk),
            data=json.dumps({'name': 'not-super-event'}),
            content_type='application/json')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(self.retrieve_uri.format(id=c.pk))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'not-super-event')
