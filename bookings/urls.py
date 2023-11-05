from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.manage_bookings, name='manage_bookings'),
    path('book/<int:id>', views.book, name='book'),
    path('booking_confirm/<int:id>', views.booking_confirm, name='booking_confirm'),
    path('delete_bookings/<int:id>', views.delete_bookings, name='delete_bookings'),
    path('update_bookings/<int:id>', views.update_bookings, name='update_bookings'),
    path('order_history', views.order_history, name='order_history'),
]