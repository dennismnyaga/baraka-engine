from rest_framework import serializers
from shop.models import *


class AllCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderItem
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    # items = OrderItemSerializer(many=True, read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    # customer = serializers.StringRelatedField()
    customer = AllCustomerSerializer(read_only=True)

    class Meta:
        model = Orders
        fields = '__all__'


