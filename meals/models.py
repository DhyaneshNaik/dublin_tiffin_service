from django.db import models


# Create your models here.
class Meals(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.IntegerField()
    image = models.ImageField(upload_to="static/meal_images/")
    is_veg = models.BooleanField()

    def __str__(self):
        return self.name