from django.db import models
from django.core.cache import cache

class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name

    def save(self):
        cache.delete('products')
        return super().save()

    def delete(self):
        cache.delete('products')
        return super().delete()
