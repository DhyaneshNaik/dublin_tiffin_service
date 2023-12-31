from django import forms
from django.contrib.auth.models import User
from .models import CustomUserAccountField


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")
        labels = {
            "username": "User Name",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email Id",
        }

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        labels = {
            "username": "User Name",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email Id",
        }


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUserAccountField
        fields = ("phone_number", "home_address", "dest_address")
        labels = {
            "phone_number": "Contact Number",
            "home_address": "Home Address",
            "dest_address": "Student/Working Address",
        }