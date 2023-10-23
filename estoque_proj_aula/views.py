from django.shortcuts import render, HttpResponse
from django.shortcuts import render, HttpResponse
from .models import Products
# Create your views here.
def index(request):
    produtos = Products.objects.all()

    # for produto in produtos:
    #     print(produto.name)
    
    return render(request, 'pages/index.html.', {'produtos':produtos})

def product_detail(request, id):
    product = Products.objects.get(id=id)
    
    return render(request, 'pages/product_detail.html',{'product':product})
