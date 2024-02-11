from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import LoginForm
# Create your views here.


def index(request):
    return render(request, "app/index.html", {})


def login(request):

    if request.method == 'GET':
        return render(request, "app/login.html", {})
    else:
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            if data['email'] and data['password']:
                return HttpResponseRedirect('/dashboard')


def dashboard(request):
    return render(request, "app/dashboard.html", {})
