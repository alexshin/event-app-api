from collections import Iterator

from ..services import EventProviderService
from hashlib import md5
from eventbrite import Eventbrite, exceptions as eventbrite_exceptions


class EventbriteProviderService(EventProviderService):

    def __init__(self, provider_id, oauth_token):
        super().__init__(provider_id)
        self.client = Eventbrite(oauth_token=oauth_token)

    @staticmethod
    def set_event_update_hash(**kwargs):
        return str(md5(kwargs['changed'].encode('utf-8')).hexdigest())

    def init_iterator(self, count=200):
        return EventbritePaginatedIterator(
            api_client=self.client,
            query_args={'expand': 'organizer,ticket_availability,category'},
            root_key='events',
            api_method='event_search',
            count=count
        )

    @staticmethod
    def clean_data_category(category):
        if category is None:
            return None

        return {
            'name': category['name']
        }

    @staticmethod
    def clean_data_organizer(organizer):
        data = {
            'name': str(organizer['name']),
            'url': organizer['url'],
            'description_plain': organizer['description'].get('text', ''),
            'description_html': organizer['description'].get('html', ''),
        }

        logo = organizer.get('logo')
        if logo:
            data['logo_uri'] = logo.get('url') or ''

        return data

    @staticmethod
    def clean_data_event(event):
        data = {
            'name':  event['name']['text'][:255],
            'uri': str(event['url']),
            'description_plain': event['description'].get('text', ''),
            'description_html': event['description'].get('html', ''),
            'ticket_price_currency': event['currency'],
            'changed': event['changed']
        }

        logo = event.get('logo')
        if logo:
            data['logo_uri'] = logo.get('url') or ''

        if event.get('start', False):
            data['start_time'] = event['start']['utc']

        if event.get('end', False):
            data['finish_time'] = event['end']['utc']

        ticket = event.get('ticket_availability', False)
        if ticket and ticket is not None:
            min_ticket_price = ticket.get('minimum_ticket_price')
            if min_ticket_price is not None:
                data['min_ticket_price'] = min_ticket_price.get('major_value')

            max_ticket_price = ticket.get('maximum_ticket_price')
            if max_ticket_price is not None:
                data['max_ticket_price'] = max_ticket_price.get('major_value')

        keys = data.keys()
        data['provider_specific_data'] = {k: v for k, v in event.items() if k not in keys}

        return data

    def process_events(self, count=200, processed_event_callback=lambda x: x):
        iter_ = self.init_iterator(count=count)
        for event in iter_:
            category_data = self.clean_data_category(event['category'])
            if category_data is None:
                category_id = None
            else:
                category_id = self.upsert_category(event['category']['id'], **category_data)

            organizer_data = self.clean_data_organizer(event['organizer'])
            organizer_id = self.upsert_organizer(event['organizer']['id'], **organizer_data)

            data = self.clean_data_event(event)

            processed_event = self.upsert_event(id_=event['id'], category_id=category_id, organizer_id=organizer_id,
                                                **data)

            processed_event_callback(processed_event)


class EventbritePaginatedIterator(Iterator):

    def __init__(self, api_client, query_args=None, count=200, root_key='events', api_method='event_search'):
        """
        Constructor
        :param api_client: Eventbrite API client
        :type api_client: Eventbrite
        :param query_args: Additional params for GET method
        :type query_args: dict
        :param count: How many records do you need to get from client
        :type count: int
        :param root_key: Root level element of response. E.g. "events" for method event_search
        :type root_key: str
        :param api_method: Method of api client to get records
        :type api_method: str
        """
        if query_args is None:
            query_args = {}

        self.api_client = api_client
        self.query_args = query_args
        self.count = count
        self.current_number = 0
        self.current_page = 0
        self.rows = None
        self.root_key = root_key
        self.api_method = getattr(api_client, api_method)

        self.result_list = []
        self.result_counter = 0
        self.result_has_next = True

        self.total_counter = 0

    def __iter__(self):
        return self

    def _get_page(self, page_number=1):
        res = self.api_method(page=page_number, **self.query_args)
        if not hasattr(res, 'status_code') or res.status_code != 200:
            raise eventbrite_exceptions.EventbriteException(f'Something goes wrong while getting new records / {res}')
        if not hasattr(res, 'pagination'):
            raise eventbrite_exceptions.EventbriteException('Iterator is waiting pagination response')
        if self.root_key not in res:
            raise eventbrite_exceptions.EventbriteException(f'Response must have "{self.root_key}" attr')

        has_next = int(res.pagination['page_count']) > page_number

        return has_next, res[self.root_key]

    def __next__(self):
        if self.total_counter >= self.count:
            raise StopIteration()

        if len(self.result_list) == 0 or self.result_counter == len(self.result_list) - 1:
            if not self.result_has_next:
                raise StopIteration()
            self.current_page += 1
            self.result_counter = 0
            self.result_has_next, self.result_list = self._get_page(page_number=self.current_page)

        item = self.result_list[self.result_counter]
        self.result_counter += 1
        self.total_counter += 1

        return item

    next = __next__
