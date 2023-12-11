from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_safe
from django.conf.urls import handler500
from .forms import SignUpForm, CustomUserForm, UserEditForm


@require_safe
def home(request):
    try:
        return render(request, 'home.html')
    except Exception:
        return redirect(handler500)

@require_safe
def aboutus(request):
    try:
        return render(request, 'aboutus.html')
    except Exception:
        return redirect(handler500)


@login_required
@transaction.atomic
@require_http_methods(["GET", "POST"])
def user_details(request):
    try:
        if request.user.is_authenticated:
            if request.method == "POST":
                user_form = UserEditForm(request.POST, instance=request.user)
                custom_user_form = CustomUserForm(request.POST, instance=request.user.customuseraccountfield)
                if user_form.is_valid() and custom_user_form.is_valid():
                    user_form.save()
                    custom_user_form.save()
                    return redirect('user_details')
                else:
                    for field in user_form.errors:
                        user_form[field].field.widget.attrs['class'] += ' error'
                    for field in custom_user_form.errors:
                        custom_user_form[field].field.widget.attrs['class'] += ' error'
                    return render(request, 'customuser/user_details.html', {"u_form": user_form, "c_form": custom_user_form})
            else:
                user_form = UserEditForm(instance=request.user)
                custom_user_form = CustomUserForm(instance=request.user.customuseraccountfield)
            return render(request, 'customuser/user_details.html', {"u_form": user_form, "c_form": custom_user_form})
    except Exception:
        return redirect(handler500)


@require_http_methods(["GET","POST"])
def login_user(request):
    try:
        if request.method == 'GET':
            return render(request, 'customuser/login.html')
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'customuser/login.html')

        return render(request, 'customuser/login.html')
    except Exception:
        return redirect(handler500)


@transaction.atomic
@require_http_methods(["GET","POST"])
def register_user(request):
    try:
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
                return redirect('login')
            else:
                user_form = SignUpForm(request.POST)
                custom_user_form = CustomUserForm(request.POST)

                for field in user_form.errors:
                    user_form[field].field.widget.attrs['class'] += ' error'
                for field in custom_user_form.errors:
                    custom_user_form[field].field.widget.attrs['class'] += ' error'
                return render(request, 'customuser/signup.html', {"u_form": user_form, "c_form": custom_user_form})
    except Exception:
        return redirect(handler500)
        

@login_required
@require_http_methods(["GET"])
def logout_user(request):
    try:
        logout(request)
        return redirect('login')
    except Exception:
        return redirect(handler500)


@require_http_methods(["GET"])
def error_404(request, exception):
    try:
        return render(request,'errors/error_404.html', status=404)
    except Exception:
        return redirect(handler500)


@require_http_methods(["GET"])
def error_500(request,):
    return render(request,'errors/error_500.html', status=500)