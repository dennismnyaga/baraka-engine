from rest_framework import serializers
from .models import *


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class ProductWeightSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductWeight
        fields = '__all__'


class SalesTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = SalesType
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    product_type = ProductTypeSerializers()
    weight = ProductWeightSerializers()
    sold_as = SalesTypeSerializers()
    
    class Meta:
        model = Product
        fields = '__all__'



class OrderDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']



class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Serialize product details if needed

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Orders
        fields = ['order_number', 'customer', 'location', 'time_ordered', 'items']