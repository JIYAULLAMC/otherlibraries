from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.permissions import AllowAny
from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(
    title="Your API",
    description = "api for the blog",
    permission_classes=(AllowAny,),  # Adjust permissions as needed
)


urlpatterns = [
    # path("admin/", admin.site.urls),
    path("api/", include('school.urls')),
    # path('api/schema/', schema_view), 
    # path("schema", schema_view, name="openapi-schema"),
    path('docs/', include_docs_urls(title='Your API Documentation')),
]
