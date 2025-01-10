from django.urls import path
from .views import ProductList ,ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('expenses/', ProductList.as_view(),  name='productslist'),
    path('createexpenses/', ProductCreateView.as_view(),  name='productscreate'),
    path('expenses/<pk>', ProductDetailView.as_view(),  name='productsdetail'),
    path('updateexpenses/<pk>', ProductUpdateView.as_view(),  name='productsupdate'),
    path('deleteexpenses/<pk>', ProductDeleteView.as_view(),  name='productsdelete'),
]