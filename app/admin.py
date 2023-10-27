from django.contrib import admin
from .models import Product

class PriceListFilter(admin.SimpleListFilter):
    title = 'Категория цен'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return (
            ('low', 'Низкая цена'),
            ('medium', 'Средняя цена'),
            ('high', 'Высокая цена'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'low':
            return queryset.filter(price__lt=100)
        elif self.value() == 'medium':
            return queryset.filter(price__gt=100, price__lte=500)
        elif self.value() == 'high':
            return queryset.filter(price__gt=500)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'country', 'type')
    fields = (('name', 'price'), 'country', 'type')
    readonly_fields = ('country',)
    search_fields = ('name',)
    list_display_links = ('name',)
    list_editable = ('price', 'type')
    list_filter = ('type',)

admin.site.register(Product, ProductAdmin)