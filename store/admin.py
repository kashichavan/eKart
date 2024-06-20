from django.contrib import admin
from django.contrib.admin import register
# Register your models here.
from .models import Product

@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','price','images','stock']


