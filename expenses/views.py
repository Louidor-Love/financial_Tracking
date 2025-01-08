from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.views.generic import View
from .models import Product



class ProductList(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {'products' : products}
        return render(request, 'expenses.html',context)
    
    
     
class ProductCreateView(View):
    def get (self, request, *args, **kwargs):
        return render(request,'expensesform.html')
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        image= request.POST.get('image')
        type = request.POST.get('type')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        Product.objects.create(name = name,image = image,type = type,price = price,quantity = quantity)
        
        return redirect('productslist') 
        

class ProductDetailView(View):
    def get (self,request,pk, *args, **kwargs):
        product = Product.objects.get(pk=pk)
        context = {'product':product}
        return render(request,'expensesdetail.html',context)








