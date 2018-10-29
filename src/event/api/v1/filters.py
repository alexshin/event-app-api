from django_filters import rest_framework as filters
from ...models import Event


class EventFilter(filters.FilterSet):
    min_start_time = filters.DateTimeFilter(field_name="start_time", lookup_expr='gte')
    max_start_time = filters.DateTimeFilter(field_name="start_time", lookup_expr='lte')

    min_finish_time = filters.DateTimeFilter(field_name="finish_time", lookup_expr='gte')
    max_finish_time = filters.DateTimeFilter(field_name="finish_time", lookup_expr='lte')

    min_ticket_price = filters.NumberFilter(field_name='min_ticket_price', lookup_expr='gte')
    max_ticket_price = filters.NumberFilter(field_name='min_ticket_price', lookup_expr='lte')

    class Meta:
        model = Event
        fields = ['start_time', 'finish_time', 'min_ticket_price', 'max_ticket_price']