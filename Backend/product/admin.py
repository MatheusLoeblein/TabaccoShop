from django.contrib import admin

from .models import Product, Variation

# Register your models here.


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_marketing', 'price_marketing_promotional']
    inlines = [VariationInline]


admin.site.register(Product, ProductAdmin)
