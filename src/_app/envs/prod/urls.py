from ..shared.urls import APPLICATION_URLS
from ..dev.urls import schema_view

from django.urls import re_path


APPLICATION_URLS += [
    re_path(
        r'^api/doc/swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=None),
        name='schema-json'
    ),
    re_path(
        r'^api/doc/$',
        schema_view.with_ui('swagger', cache_timeout=None),
        name='schema-swagger-ui'
    )
]
