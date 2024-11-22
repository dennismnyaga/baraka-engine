from rest_framework import serializers
from shop.models import *


class AllCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'