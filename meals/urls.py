from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.meals, name='meals'),
    path('meal_form_add_update/', views.meal_form_add_update, name='add_meal'),
    path('meal_form_add_update/<int:id>', views.meal_form_add_update, name='meal_form_add_update'),
    path('delete_meal/<int:id>', views.delete_meal, name='delete_meal')
]
