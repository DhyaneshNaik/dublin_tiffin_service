from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class CustomUserAccountField(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    home_address = models.CharField(max_length=100)
    dest_address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUserAccountField.objects.create(user=instance)