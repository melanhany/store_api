from rest_framework.pagination import PageNumberPagination
from .models import Product

class DefaultPagination(PageNumberPagination):
    page_size = 10