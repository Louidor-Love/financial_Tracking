from django.shortcuts import render
from django.shortcuts import render ,redirect ,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from expenses.models import Product
from users.models import Perfil
from django.db.models import Q


# Create your views here.

class Dashboard(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        #dashboard
        pk = kwargs.get('pk')
        products = Product.objects.filter(user=request.user)
        perfil = Perfil.objects.get(user=request.user)

        #search bar
        queryset = request.GET.get('q')
        if queryset:
            products = Product.objects.filter(
                Q(name__icontains=queryset) |
                Q(description__icontains=queryset) |
                Q(type__icontains=queryset)
            )

        context = {'products' : products , 'perfil':perfil}
        return render(request, 'dashboard.html',context)
    
  


