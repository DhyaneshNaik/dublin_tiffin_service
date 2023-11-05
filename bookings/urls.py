from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.manage_bookings, name='manage_bookings'),
    path('order_history', views.order_history, name='order_history'),
]