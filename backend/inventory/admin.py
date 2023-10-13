from django.contrib import admin
from .models import Inventory, Brand, Room

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'date', 'qty', 'unit', 'breakages', 'balance', 'remarks', 'room')
    search_fields = ('name', 'brand__name', 'room__name')

admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Brand)
admin.site.register(Room)
