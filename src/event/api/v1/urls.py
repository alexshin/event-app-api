from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, OrganizerViewSet, EventViewSet


router = DefaultRouter()
router.register(r'api/v1/categories', CategoryViewSet, base_name='category')
router.register(r'api/v1/organizers', OrganizerViewSet, base_name='organizer')
router.register(r'api/v1/events', EventViewSet, base_name='event')

urlpatterns = router.urls
