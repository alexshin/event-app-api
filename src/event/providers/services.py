from abc import ABCMeta, abstractmethod
from ..models import Category, Organizer, Event


class EventProviderService(metaclass=ABCMeta):

    _update_cache = {
        'category': dict(),
        'organizer': dict(),
    }

    category_class = Category
    organizer_class = Organizer
    event_class = Event

    organizer_attributes = ('name', 'uri', 'description_plain', 'description_html', 'logo_uri')
    category_attributes = ('name',)
    event_attributes = ('name', 'uri', 'description_plain', 'description_html', 'start_time', 'finish_time',
                        'logo_uri', 'min_ticket_price', 'max_ticket_price', 'ticket_price_currency',
                        'provider_specific_data')

    def __init__(self, provider_id: int):
        self.provider_id = provider_id

    def upsert_category(self, id_: str, **kwargs):
        if id_ in self._update_cache['category']:
            return self._update_cache['category'].get(id_)

        category = self.category_class.objects.filter(provider=self.provider_id, provider_object_id=id_)

        if category.exists():
            category = category.get()
        else:
            category = self.category_class(provider=self.provider_id, provider_object_id=id_)

        category.is_actual = True
        for k, v in kwargs.items():
            if k in self.organizer_attributes:
                setattr(category, k, v)

        category.save()

        self._update_cache['category'][id_] = category.pk

        return category.pk

    def upsert_organizer(self, id_: str, **kwargs):
        if id_ in self._update_cache['organizer']:
            return self._update_cache['organizer'].get(id_)

        organizer = self.organizer_class.objects.filter(provider=self.provider_id, provider_object_id=id_)

        if organizer.exists():
            organizer = organizer.get()
        else:
            organizer = self.organizer_class(provider=self.provider_id, provider_object_id=id_)

        organizer.is_actual = True
        for k, v in kwargs.items():
            if k in self.organizer_attributes:
                setattr(organizer, k, v)

        organizer.save()

        self._update_cache['organizer'][id_] = organizer.pk

        return organizer.pk

    @staticmethod
    @abstractmethod
    def set_event_update_hash(**kwargs) -> str:
        pass

    def upsert_event(self, id_: str, category_id, organizer_id, **kwargs):
        update_hash = self.set_event_update_hash(**kwargs)

        event = self.event_class.objects.filter(provider=self.provider_id, provider_object_id=id_)
        if event.exists():
            event = event.get()
            if event.changed_by_provider_hash == update_hash:
                return event
        else:
            event = self.event_class(provider=self.provider_id, provider_object_id=id_)

        event.is_actual = True
        event.category_id = category_id
        event.organizer_id = organizer_id
        event.changed_by_provider_hash = self.set_event_update_hash(**kwargs)

        for k, v in kwargs.items():
            if k in self.event_attributes:
                setattr(event, k, v)

        event.save()

        return event
