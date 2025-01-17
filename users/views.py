from django.shortcuts import render,redirect
from expenses.views import *
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse

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
                login(request ,user)
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
