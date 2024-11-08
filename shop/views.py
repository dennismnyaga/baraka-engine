from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from.models import *

# Create your views here.

class all_products(APIView):
    def get(self, request):
        products = Product.objects.all()
        serialize = ProductSerializers(products, many=True)

        return Response(serialize.data)
    

class single_product(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serialize = ProductSerializers(product)

        return Response(serialize.data)