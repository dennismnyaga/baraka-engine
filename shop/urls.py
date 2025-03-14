from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_products.as_view()),
    path('details/<str:pk>/', views.single_product.as_view()),
    path('addorder/', views.process_order.as_view()),
    path('analytics/', views.DataVisualization.as_view())
]
