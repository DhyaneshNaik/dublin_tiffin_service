from django.db import models
from meals.models import Meals
from django.contrib.auth.models import User

# Create your models here.
class Bookings(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_id = models.ForeignKey(Meals, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_cost = models.FloatField()
    is_delievered = models.BooleanField()