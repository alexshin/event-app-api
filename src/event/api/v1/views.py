from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from utils.viewset_mixins import ChangeOnlyViewSet
from .serializers import CategorySerializer, CategoryUpdateSerializer, \
    OrganizerListSerializer, OrganizerDetailSerializer, OrganizerUpdateSerializer, \
    EventListSerializer, EventDetailSerializer, EventUpdateSerializer
from ...models import Category, Organizer, Event
from .filters import EventFilter


class CategoryViewSet(ChangeOnlyViewSet):
    queryset = Category.objects.all()

    def get_serializer_class_for_list(self):
        return CategorySerializer

    def get_serializer_class_for_detail(self):
        return CategorySerializer

    def get_serializer_class_for_update(self):
        return CategoryUpdateSerializer


class OrganizerViewSet(ChangeOnlyViewSet):
    queryset = Organizer.objects.all()

    def get_serializer_class_for_detail(self):
        return OrganizerDetailSerializer

    def get_serializer_class_for_list(self):
        return OrganizerListSerializer

    def get_serializer_class_for_update(self):
        return OrganizerUpdateSerializer


class EventViewSet(ChangeOnlyViewSet):
    queryset = Event.objects.all()

    def get_serializer_class_for_list(self):
        return EventListSerializer

    def get_serializer_class_for_detail(self):
        return EventDetailSerializer

    def get_serializer_class_for_update(self):
        return EventUpdateSerializer


class SearchEventView(generics.ListAPIView):
    queryset = Event.objects.prefetch_related('category', 'organizer').all()
    serializer_class = EventListSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,)
    filter_fields = ('provider', 'category', 'organizer')
    search_fields = ('name', 'category__name', 'organizer__name')
    filterset_class = EventFilter

