from django.shortcuts import render

# Create your views here.


def manage_bookings(request):
    return render(request, 'bookings/manage_bookings.html')

def order_history(request):
    return render(request, 'bookings/order_history.html')