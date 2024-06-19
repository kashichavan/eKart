from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Category
# Register your models here.
@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['category_name','slug','description','cat_image']
