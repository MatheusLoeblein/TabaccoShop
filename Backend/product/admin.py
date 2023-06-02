from django.contrib import admin

from .models import Product, Variation

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    ...


class VariationAdmin(admin.ModelAdmin):
    ...


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
