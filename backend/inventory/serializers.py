from rest_framework import serializers
from .models import Inventory, Brand, Room

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = '__all__'
