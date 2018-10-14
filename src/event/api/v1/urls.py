from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, OrganizerViewSet, EventViewSet


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, base_name='category')
router.register(r'organizers', OrganizerViewSet, base_name='organizer')
router.register(r'events', EventViewSet, base_name='event')

urlpatterns = router.urls
