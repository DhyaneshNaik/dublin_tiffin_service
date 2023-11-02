from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.meals, name='meals'),
    path('add_meal', views.add_meal, name='add_meal')
]