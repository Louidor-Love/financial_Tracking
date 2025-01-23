from django.shortcuts import render, redirect
from expenses.views import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from .models import Perfil

# Create your views here.


def signup(request):
    if request.method == 'GET':
        context = {'form': UserCreationForm}
        return render(request, 'signup.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                if 'foto' in request.FILES:
                    perfil = Perfil.objects.create(
                        user=user, foto=request.FILES.get('foto'))

                return redirect('productslist')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'username already exist'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'password do not match'
        })


def signout(request):
    logout(request)
    return redirect('productslist')


def signin(request):
    if request.method == 'GET':
        context = {'form': AuthenticationForm}
        return render(request, 'signin.html', context)
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                "error": 'username or password is incorrect'
            })
        else:
            print(request.POST.get('password'))
            login(request, user)
            return redirect('productslist')

