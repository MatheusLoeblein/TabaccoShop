from django.contrib import admin

from .models import ItemOrder, Order


class OrderAdmin(admin.ModelAdmin):
    ...


class ItemOrderAdmin(admin.ModelAdmin):
    ...


admin.site.register(Order, OrderAdmin)
admin.site.register(ItemOrder, ItemOrderAdmin)
