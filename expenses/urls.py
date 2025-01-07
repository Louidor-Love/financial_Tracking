from django.urls import path
from .views import ProductList ,ProductCreateView

urlpatterns = [
    path('expenses/', ProductList.as_view(),  name='productslist'),
    path('createexpenses/', ProductCreateView.as_view(),  name='productscreate'),
]