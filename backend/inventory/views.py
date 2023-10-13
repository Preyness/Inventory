from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Inventory, Brand, Room
from django.views.generic import ListView
from .models import Inventory

class InventoryListView(ListView):
    model = Inventory
    template_name = 'inventory_list.html'
    context_object_name = 'inventory_list'

class GlasswareListView(ListView):  # New view for Glassware
    model = Inventory
    template_name = 'glassware_list.html'  # Update with your actual template name
    context_object_name = 'glassware_list'

    def get_queryset(self):
        return Inventory.objects.filter(category__name='Glassware')

class MiscellaneousListView(ListView):  # New view for Miscellaneous
    model = Inventory
    template_name = 'miscellaneous_list.html'  # Update with your actual template name
    context_object_name = 'miscellaneous_list'

    def get_queryset(self):
        return Inventory.objects.filter(category__name='Miscellaneous')

class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'inventory_detail.html'
    context_object_name = 'inventory'

class BrandListView(ListView):
    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brand_list'

class BrandDetailView(DetailView):
    model = Brand
    template_name = 'brand_detail.html'
    context_object_name = 'brand'

class RoomListView(ListView):
    model = Room
    template_name = 'room_list.html'
    context_object_name = 'room_list'

class RoomDetailView(DetailView):
    model = Room
    template_name = 'room_detail.html'
    context_object_name = 'room'
