from django.shortcuts import render
from store.models import Product

def index(request):
    return render(request,'index.html')

def cart(request):
    return render(request,'cart.html')

def store(request):
    allproducts=Product.objects.filter( is_avaiable=True)
    data={'data':allproducts}
    return render(request,'store.html',data)