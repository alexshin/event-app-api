from utils.viewset_mixins import ChangeOnlyViewSet
from .serializers import CategorySerializer, CategoryUpdateSerializer, \
    OrganizerListSerializer, OrganizerDetailSerializer, OrganizerUpdateSerializer, \
    EventListSerializer, EventDetailSerializer, EventUpdateSerializer
from ...models import Category, Organizer, Event


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
