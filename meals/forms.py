from django import forms
from .models import Meals


class MealsForm(forms.ModelForm):
    class Meta:
        model = Meals
        fields = ("name", "description", "cost", "image", "is_veg")
        labels = {
            "name": "Dish Name",
            "description": "Description",
            "cost": "Amount",
            "image": "Image",
            "is_veg": "Veg/Non-Veg"
        }