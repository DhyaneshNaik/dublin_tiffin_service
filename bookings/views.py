from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from meals.models import Meals
from .models import Bookings

# Create your views here.


def book(request, id):
    data = Meals.objects.get(id=id)
    return render(request, 'bookings/book.html', {'meal': data})

def booking_confirm(request, id):
    meal = Meals.objects.get(id=id)
    total_cost = request.POST.get('total_cost')
    quantity = request.POST.get('quantity')
    user = User.objects.get(id=request.user.id)

    booking = Bookings(user_id=user, meal_id=meal, quantity=quantity, total_cost=total_cost, is_delievered=False)
    booking.save()

    return redirect('manage_bookings')
    # return render(request, 'bookings/book.html', {'meal': data})

def manage_bookings(request):
    data = Bookings.objects.filter(is_delievered=False)
    return render(request, 'bookings/manage_bookings.html', {'bookings': data})

def delete_bookings(request, id):
    data = Bookings.objects.get(id=id)
    data.delete()

    data = Bookings.objects.filter(is_delievered=False)
    return render(request, 'bookings/manage_bookings.html', {'bookings': data})

def update_bookings(request, id):
    data = Bookings.objects.get(id=id)
    data.is_delievered = True
    data.save()

    data = Bookings.objects.filter(is_delievered=False)
    return render(request, 'bookings/manage_bookings.html', {'bookings': data})

def order_history(request):
    data = Bookings.objects.filter(is_delievered=True)
    return render(request, 'bookings/order_history.html', {'bookings': data})