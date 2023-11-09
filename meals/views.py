from django.shortcuts import render, redirect
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

def delete_meal(request, id):
    if request.method == 'GET':
        meal = Meals.objects.get(id=id)
        meal.delete()
        veg_meal = Meals.objects.filter(is_veg=True)
        nonveg_meal = Meals.objects.filter(is_veg=False)
        return render(request, 'meals/meals.html', {"veg_meal": veg_meal, "nonveg_meal": nonveg_meal })
    if request.method == 'POST':
        print("POST")
        return render(request, 'meals/meals.html')

def meal_form_add_update(request, id=0):
    if request.method == 'GET':
        if id == 0:
            m_form = MealsForm()
        else:
            meal = Meals.objects.get(id=id)
            m_form = MealsForm(instance=meal)
        return render(request, 'meals/meal_form.html', {'m_form': m_form})
    if request.method == 'POST':
        if id==0:
            m_form = MealsForm(request.POST, request.FILES)
        else:
            meal = Meals.objects.get(id=id)
            m_form = MealsForm(request.POST, instance=meal)
        if m_form.is_valid():
            m_form.save()
        print(m_form.errors)
        return redirect('meals')
    return render(request, 'meals/add_meal.html')