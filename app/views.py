from django.shortcuts import render
from django.http import HttpResponseRedirect
from random import randint

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
    social_media_accounts_names = [
        'facebook', 'twitter', 'instagram', 'youtube']

    social_media_alias = {
        'facebook': 'Test Business',
        'twitter': '@testBusiness134',
        'instagram': 'test_business__',
        'youtube': 'test_buseness'

    }

    social_media_accounts = [{
        'name': name.capitalize(),
        'account': social_media_alias[name],
        'id': name,
        'followers': randint(100, 500),
        'icon': "/app/assets/ic-%s.svg" % name
    } for name in social_media_accounts_names]

    return render(request, "app/dashboard.html", {"accounts": social_media_accounts})
