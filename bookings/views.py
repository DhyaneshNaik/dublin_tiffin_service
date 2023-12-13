from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.conf.urls import handler500
from meals.models import Meals
from .models import Bookings


@login_required
@require_http_methods(["GET"])
def book(request, id):
    try:
        data = Meals.objects.get(id=id)
        return render(request, 'bookings/book.html', {'meal': data})
    except Exception:
        return redirect(handler500)


@login_required
@require_http_methods(["POST"])
def booking_confirm(request, id):
    try:
        meal = Meals.objects.get(id=id)
        total_cost = request.POST.get('total_cost')
        quantity = request.POST.get('quantity')
        user = User.objects.get(id=request.user.id)

        booking = Bookings(user_id=user, meal_id=meal, quantity=quantity, total_cost=total_cost, is_delievered=False)
        booking.save()

        return redirect('manage_bookings')
    except Exception:
        return redirect(handler500)
    

@login_required
@require_http_methods(["GET"])
def manage_bookings(request):
    try:
        if request.user.username == 'admin':
            data = Bookings.objects.filter(is_delievered=False)
        else:
            data = Bookings.objects.filter(is_delievered=False, user_id=request.user.id)
        return render(request, 'bookings/manage_bookings.html', {'bookings': data})
    except Exception:
        return redirect(handler500)
    

@login_required
@require_http_methods(["GET"])
def delete_bookings(request, id):
    try:
        if request.user.username == 'admin':
            data = Bookings.objects.get(id=id)
        else:
            data = Bookings.objects.get(id=id, user_id=request.user.id)
        data.delete()
        return redirect("manage_bookings")
    except Exception:
        return redirect(handler500)


@login_required
@require_http_methods(["GET"])
def update_bookings(request, id):
    try:
        if request.user.username == 'admin':
            data = Bookings.objects.get(id=id)
            data.is_delievered = True
            data.save()

            data = Bookings.objects.filter(is_delievered=False)
            return render(request, 'bookings/manage_bookings.html', {'bookings': data})
        else:
            return redirect("manage_bookings")
    except Exception:
        return redirect(handler500)


@login_required
@require_http_methods(["GET"])
def order_history(request):
    try:
        if request.user.username == 'admin':
            data = Bookings.objects.filter(is_delievered=True)
        else:
            data = Bookings.objects.filter(is_delievered=True, user_id=request.user.id)
        return render(request, 'bookings/order_history.html', {'bookings': data})
    except Exception:
        return redirect(handler500)


