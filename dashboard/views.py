from django.shortcuts import render
from django.shortcuts import render ,redirect ,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from expenses.models import Product
from users.models import Perfil


# Create your views here.

class Dashboard(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        perfil = Perfil.objects.get(user=request.user)
        context = {'products' : products , 'perfil':perfil}
        return render(request, 'dashboard.html',context)