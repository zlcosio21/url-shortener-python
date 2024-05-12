from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("shortener.urls")),
    path('api/', include("api.urls")),
    path('api/documentation', include_docs_urls(title="API Documentation")),
]
