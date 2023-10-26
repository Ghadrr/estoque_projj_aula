from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.index, name='home'),
    path('product-detail/<int:id>/', views.product_detail , name='product-detail'),
    path('add-product/', views.add_product, name='add_product'),
    path('delete-product/<int:id>/', views.delete_product, name='delete_product')
    
]