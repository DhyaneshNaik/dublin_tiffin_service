from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import CustomUserAccountField

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUserAccountField
        fields = ("phone_number", "home_address", "dest_address")


# Create your views here.
def home(request):
    return render(request, 'home.html')


def aboutus(request):
    return render(request, 'aboutus.html')


@login_required
@transaction.atomic
def user_details(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user_form = UserForm(request.POST, instance=request.user)
            custom_user_form = CustomUserForm(request.POST, instance=request.user.customuseraccountfield)
            if user_form.is_valid() and custom_user_form.is_valid():
                user_form.save()
                custom_user_form.save()
                return redirect('user_details')
            else:
                pass #add exception hanndling for forms.
        else:
            user_form = UserForm(instance=request.user)
            custom_user_form = CustomUserForm(instance=request.user.customuseraccountfield)
        return render(request, 'customuser/user_details.html', {"u_form": user_form, "c_form": custom_user_form})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'customuser/login.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = authenticate(username=email, password=password)
        if user is not None:
            print('login')
            login(request, user)
            return redirect('home')
        else:
            print('Login failed')
            return render(request, 'customuser/login.html')

    return render(request, 'customuser/login.html')


@transaction.atomic
def register_user(request):
    if request.method == 'GET':
        user_form = UserForm()
        custom_user_form = CustomUserForm()
        return render(request, 'customuser/signup.html', {"u_form": user_form, "c_form": custom_user_form})
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        custom_user_form = CustomUserForm(request.POST)

        print(user_form.is_valid() , custom_user_form.is_valid())
        
        if user_form.is_valid() and custom_user_form.is_valid():
            user = user_form.save()
            print('saved 2')

            custom_user = custom_user_form.save(commit=False)
            custom_user.user = user
            custom_user.save()
            print('saved 3')
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username, password)
            user = authenticate(username=username, passsword=password)
            return redirect('login')
        else:
            user_form = UserForm(request.POST)
            custom_user_form = CustomUserForm(request.POST)
            return render(request, 'customuser/signup.html', {"u_form": user_form, "c_form": custom_user_form})
        


def logout_user(request):
    logout(request)
    return redirect('login')