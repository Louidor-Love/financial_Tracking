from django.contrib import admin
from django.urls import path,include 

urlpatterns = [
    path('financial_admin/', admin.site.urls),
    path('', include('expenses.urls')),
   
]
