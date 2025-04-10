from django.urls import path
from .views import dashboard, orders

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('orders/', orders, name='orders'),
]