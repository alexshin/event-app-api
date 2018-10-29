from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, OrganizerViewSet, EventViewSet, SearchEventView


router = DefaultRouter()
router.register(r'api/v1/categories', CategoryViewSet, base_name='category')
router.register(r'api/v1/organizers', OrganizerViewSet, base_name='organizer')
router.register(r'api/v1/events', EventViewSet, base_name='event')

urlpatterns = router.urls

urlpatterns += [
    path('api/v1/events/search', SearchEventView.as_view(), name='api-v1-event-search'),
]