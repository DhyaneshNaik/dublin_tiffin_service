from django.shortcuts import render
from .forms import MealsForm
from .models import Meals
# Create your views here.


def meals(request):
    if request.method == 'GET':
        veg_meal = Meals.objects.filter(is_veg=True)
        nonveg_meal = Meals.objects.filter(is_veg=False)
        return render(request, 'meals/meals.html', {"veg_meal": veg_meal, "nonveg_meal": nonveg_meal })
    if request.method == 'POST':
        return render(request, 'meals/meals.html')


def add_meal(request):
    return render(request, 'meals/add_meal.html')