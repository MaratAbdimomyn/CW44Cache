from django.shortcuts import render
from django.views.generic import ListView
from django.core.cache import cache
from .models import *

class ListProducts(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'home.html'

    def get_queryset(self):
        
        products = cache.get('products')

        if products is None:
            products = Product.objects.all()
            cache.set('products', products, 60)

        return products