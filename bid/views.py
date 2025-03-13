from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from .models import Bid, AutoPlate, User


def home(request):
    plates = AutoPlate.objects.all()
    return render(request, 'home.html', {"plates": plates})


def login_view(request):
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
        return render(request, 'login/login.html', {
            "form": forms
        })
    forms = LoginForm()
    return render(request, 'login/login.html', {
        "forms": forms
    })


def register(request):
    if request.method == "POST":
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            user = forms.save()
            login(request, user)
            return redirect('login_view')
        return render(request, 'login/register.html', {"forms": forms})
    forms = RegisterForm()
    return render(request, 'login/register.html', {"forms": forms})


def logout_view(request):
    logout(request)
    return redirect('login_view')


def bids(request):
    pass
