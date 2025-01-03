from django.contrib import admin
from .models import Product ,Expenses ,Detail_Expenses


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('image','name','type','price','quantity')
    
@admin.register(Expenses)
class ExpensesModelAdmin(admin.ModelAdmin):
    list_display = ('get_product_name','price_total')

admin.site.register(Detail_Expenses)


