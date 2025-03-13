from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegisterForm
from .models import Bid, AutoPlate, User


def home(request):
    q = request.GET.get('q', '')
    plates = AutoPlate.objects.all()

    if q and q != "None":
        plates = AutoPlate.objects.search(q)

    data = {"plates": plates, "q": q}

    return render(request, 'home.html', context=data)


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
    bid = Bid.objects.all()
    return render(request, "bids/bids.html", {"bid": bid})


def plates(request):
    q = request.GET.get('q', '')
    plate = AutoPlate.objects.all()

    if q and q != "None":
        plate = AutoPlate.objects.search(q)

    data = {"plate": plate, "q": q}
    return render(request, 'plates/plates.html', context=data)


def plate_detail(request, pk):
    plate = get_object_or_404(AutoPlate, pk=pk)
    return render(request, 'plates/detail_plate.html', {"plate": plate})
