from ..shared.urls import APPLICATION_URLS

from django.urls import re_path, include, path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Events-app API",
        default_version='v1',
        description="API to create and manage Event-app",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="alex.shinkevich@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

APPLICATION_URLS += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    path('api-auth/', include('rest_framework.urls'))
]