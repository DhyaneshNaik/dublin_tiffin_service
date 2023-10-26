from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomUserAccountField(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    home_address = models.CharField(max_length=100)
    dest_address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username