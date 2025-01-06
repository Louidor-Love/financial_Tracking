from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import Product

# Create your views here.

class ProductList(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {'products' : products}
        return render(request, 'expenses.html',context )







