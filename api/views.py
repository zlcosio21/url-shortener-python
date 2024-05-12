from rest_framework import viewsets
from shortener.models import UrlShortener
from .serializer import UrlShortenerSerializer
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class UrlShortenerPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class UrlShortenerAllViewSet(viewsets.ModelViewSet):
    queryset = UrlShortener.objects.all()
    serializer_class = UrlShortenerSerializer

class UrlShortenerViewSet(viewsets.ModelViewSet):
    queryset = UrlShortener.objects.all()
    serializer_class = UrlShortenerSerializer
    pagination_class = UrlShortenerPagination