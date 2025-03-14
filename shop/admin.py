from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(ProductType)
admin.site.register(ProductWeight)
admin.site.register(SalesType)
admin.site.register(Customer)
admin.site.register(Orders)
admin.site.register(OrderItem)
admin.site.register(Shop)
admin.site.register(SalesRecord)