from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from.models import *
from shop.serializers import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 20  # Override global page size
    page_size_query_param = 'page_size'  # Allow clients to specify page size
    max_page_size = 100  # Optional: Limit the maximum page size




# Create your views here.

class all_products(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class all_customers(ListAPIView):
    queryset = Customer.objects.order_by("-date_added")
    serializer_class = AllCustomerSerializer
    pagination_class = CustomPagination