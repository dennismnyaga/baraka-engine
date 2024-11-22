from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_products.as_view()),
    path('customers', views.all_customers.as_view()),
]
