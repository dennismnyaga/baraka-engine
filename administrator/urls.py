from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_products.as_view()),
    path('customers/', views.all_customers.as_view()),
    path('orders/', views.OrderViewSet.as_view()),
    path('orders/<int:order_id>/update-status/', views.UpdateOrderStatusView.as_view(), name='update-order-status'),
]
