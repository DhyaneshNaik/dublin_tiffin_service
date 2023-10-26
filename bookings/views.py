from django.shortcuts import render

# Create your views here.


def bookings(request):
    return render(request, 'bookings/bookings.html')

def order_history(request):
    return render(request, 'bookings/order_history.html')