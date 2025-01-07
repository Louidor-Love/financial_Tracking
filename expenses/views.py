from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.views.generic import View
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class ProductList(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {'products' : products}
        return render(request, 'expenses.html',context)
    
@method_decorator(csrf_exempt, name='dispatch')    
class ProductCreateView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        image= request.POST.get('image')
        type = request.POST.get('type')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        Product.objects.create(name = name,image = image,type = type,price = price,quantity = quantity)
        
        return redirect('productslist') 
        

           







