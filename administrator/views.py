from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, get_object_or_404

from rest_framework.viewsets import ModelViewSet
from .models import *
from shop.serializers import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 20  # Override global page size
    page_size_query_param = 'page_size'  # Allow clients to specify page size
    max_page_size = 100  # Optional: Limit the maximum page size




# Create your views here.

class OrderViewSet(APIView):
    def get(self, request):
        orders = Orders.objects.all()
        serialize = OrdersSerializer(orders, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)



class all_products(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class all_customers(ListAPIView):
    queryset = Customer.objects.order_by("-date_added")
    serializer_class = AllCustomerSerializer
    pagination_class = CustomPagination



class UpdateOrderStatusView(APIView):
    def put(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Orders, id=order_id)
        order.dispatched = request.data.get('dispatched', order.dispatched)
        order.save()
        serializer = OrdersSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)