from rest_framework.serializers import ModelSerializer
from ...models import Category, Organizer, Event


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'provider')


class CategoryUpdateSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class OrganizerListSerializer(ModelSerializer):
    class Meta:
        model = Organizer
        fields = ['id', 'name', 'uri', 'logo_uri', 'provider']


class OrganizerDetailSerializer(OrganizerListSerializer):
    class Meta(OrganizerListSerializer.Meta):
        fields = OrganizerListSerializer.Meta.fields + ['description_plain', 'description_html']


class OrganizerUpdateSerializer(ModelSerializer):
    class Meta(OrganizerDetailSerializer.Meta):
        fields = ['name', 'uri', 'logo_uri', 'description_plain', 'description_html']


class EventListSerializer(ModelSerializer):
    category = CategorySerializer()
    organizer = OrganizerListSerializer()

    class Meta:
        model = Event
        fields = ['id', 'provider', 'name', 'uri', 'category', 'organizer', 'start_time', 'finish_time',
                  'ticket_price_currency', 'min_ticket_price', 'max_ticket_price', 'logo_uri']


class EventDetailSerializer(EventListSerializer):
    class Meta(EventListSerializer.Meta):
        fields = EventListSerializer.Meta.fields + ['description_plain', 'description_html', 'provider_specific_data']


class EventUpdateSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'uri', 'logo_uri', 'ticket_price_currency', 'min_ticket_price', 'max_ticket_price',
                  'logo_uri')
