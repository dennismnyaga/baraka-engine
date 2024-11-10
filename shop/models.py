from django.db import models
import uuid
import random

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
    

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=15)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name or ''}".strip()


class Orders(models.Model):
    order_number = models.IntegerField(unique=True)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    time_ordered = models.DateTimeField(auto_now_add=True)
    dispatched = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.order_number} by {self.customer}"
    
    # def save(self, *args, **kwargs):
    #     if not self.order_number:
    #         # Generate a random 4-digit number until a unique number is found
    #         while True:
    #             random_number = random.randint(1000, 9999)
    #             if not Orders.objects.filter(order_number=random_number).exists():
    #                 self.order_number = random_number
    #                 break
    #     super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for Order {self.order.order_number}"