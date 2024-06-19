from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def cart(request):
    return render(request,'cart.html')