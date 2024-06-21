from django.urls import path
from .views import *
app_name='store'

urlpatterns = [
    path('',store,name='store'),
    path('<slug:category_slug>/',store,name='store'),


]
