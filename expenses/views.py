from django.shortcuts import render ,redirect ,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import Product



class ProductList(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {'products' : products}
        return render(request, 'expenses.html',context)
    
class ProductUpdate(LoginRequiredMixin,View):
    def get(self, request,pk, *args, **kwargs):
        product = Product.objects.get(pk=pk)
        context = {'product' : product}
        return render(request, 'expensesupdate.html',context)
    
    
     
class ProductCreateView(LoginRequiredMixin,View):
    def get (self, request, *args, **kwargs):
        return render(request,'expensesform.html')
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        image = request.FILES.get('image')
        type = request.POST.get('type')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        user = request.user
        Product.objects.create(name = name,image = image,type = type,price = price,quantity = quantity,description = description, user=user)
        
        return redirect('productslist') 
    
class ProductUpdateView(LoginRequiredMixin,View):
    def get (self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.get(pk=pk)
        context = {'product':product}
        return render(request,'expensesform.html', context)
    
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.get(pk=pk)
        product.name = request.POST.get('name')
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.type = request.POST.get('type')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.description = request.POST.get('description')
        product.user = request.user
        product.save()
        print(request.FILES['image'])
        
        return redirect('productslist')    

class ProductDeleteView(LoginRequiredMixin,View):
    def get (self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.get(pk=pk)
        context = {'product':product}
        return render(request,'expenses_confirmdelete.html', context)
    
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.get(pk=pk)
        product.delete()
        
        return redirect('productslist')      
        

class ProductDetailView(LoginRequiredMixin,View):
    def get (self,request,pk, *args, **kwargs):
        product = Product.objects.get(pk=pk)
        context = {'product':product}
        return render(request,'expensesdetail.html',context)








