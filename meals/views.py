from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.conf.urls import handler500
from .forms import MealsForm
from .models import Meals


@login_required
@require_http_methods(["GET", "POST"])
def meals(request):
    try:
        if request.method == 'GET':
            veg_meal = Meals.objects.filter(is_veg=True)
            nonveg_meal = Meals.objects.filter(is_veg=False)
            return render(request, 'meals/meals.html', {"veg_meal": veg_meal, "nonveg_meal": nonveg_meal })
        if request.method == 'POST':
            return render(request, 'meals/meals.html')
    except Exception:
        return redirect(handler500)


@login_required
@require_http_methods(["GET", "POST"])
def delete_meal(request, id):
    try:
        if request.method == 'GET':
            meal = Meals.objects.get(id=id)
            meal.delete()
            veg_meal = Meals.objects.filter(is_veg=True)
            nonveg_meal = Meals.objects.filter(is_veg=False)
            return render(request, 'meals/meals.html', {"veg_meal": veg_meal, "nonveg_meal": nonveg_meal })
        if request.method == 'POST':
            return render(request, 'meals/meals.html')
    except Exception:
        return redirect(handler500)


@login_required
@require_http_methods(["GET", "POST"])
def meal_form_add_update(request, id=0):
    try:
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
            else:
                for field in m_form.errors:
                    m_form[field].field.widget.attrs['class'] += ' error'
                return render(request, 'meals/meal_form.html', {'m_form': m_form})
            return redirect('meals')
        return render(request, 'meals/add_meal.html')
    except Exception:
        return redirect(handler500)
