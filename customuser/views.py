from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, CustomUserForm, UserEditForm



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
            user_form = UserEditForm(request.POST, instance=request.user)
            custom_user_form = CustomUserForm(request.POST, instance=request.user.customuseraccountfield)
            print(user_form.is_valid(), custom_user_form.is_valid())
            if user_form.is_valid() and custom_user_form.is_valid():
                print('save 1')
                user_form.save()
                print('save 2')
                custom_user_form.save()
                print('save 3')
                return redirect('user_details')
            else:
                print(user_form.errors)
                pass #add exception hanndling for forms.
        else:
            user_form = UserEditForm(instance=request.user)
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
        user_form = SignUpForm()
        custom_user_form = CustomUserForm()
        return render(request, 'customuser/signup.html', {"u_form": user_form, "c_form": custom_user_form})
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        custom_user_form = CustomUserForm(request.POST)

        if user_form.is_valid() and custom_user_form.is_valid():
            user = user_form.save()

            custom_user = custom_user_form.save(commit=False)
            custom_user.user = user
            custom_user.save()
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            return redirect('login')
        else:
            user_form = SignUpForm(request.POST)
            custom_user_form = CustomUserForm(request.POST)
            return render(request, 'customuser/signup.html', {"u_form": user_form, "c_form": custom_user_form})
        


def logout_user(request):
    logout(request)
    return redirect('login')