from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

# Create your views here.
def salud(request):
    return HttpResponse(f"<p> El número es {1234} </p")
