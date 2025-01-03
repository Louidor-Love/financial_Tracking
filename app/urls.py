from django.contrib import admin
from django.urls import path,include 

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('financial_admin/', admin.site.urls),
    path('', include('expenses.urls')),
]
