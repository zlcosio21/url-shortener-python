from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"all_urls", views.UrlShortenerAllViewSet)
router.register(r"urls", views.UrlShortenerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
