from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def salud(request):
    return HttpResponse(f"<p> El número es {1234} </p")
