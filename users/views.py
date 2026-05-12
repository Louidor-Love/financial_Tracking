from django.shortcuts import render, redirect
from expenses.views import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from .models import Perfil

# Create your views here.

# vista de signup
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

# vista de signout
def signout(request):
    logout(request)
    return redirect('productslist')

# vista de signin
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
            # crea sesion normal
            login(request, user)
            #crear token
            refresh = RefreshToken.for_user(user)
            #convierte el token a string para reutilizar
            access_token = str(refresh.access_token)
            response = redirect('productslist')
            response.set_cookie(key='access_token', value=access_token )
            return response 

