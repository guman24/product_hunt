from django.contrib import admin
from django.urls import path
from products.views import create,detail

urlpatterns = [
    path('create',create,name='create'),
     path('<int:product_id>',detail,name='detail'),
]
