from django.db import models
import uuid

# Create your models here.
class Brand(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ProductType(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class ProductWeight(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    weight = models.CharField(max_length=50)

    def __str__(self):
        return self.weight
    
class SalesType(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    weight = models.ForeignKey(ProductWeight, on_delete=models.CASCADE, blank=True, null=True)
    sold_as = models.ForeignKey(SalesType, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
