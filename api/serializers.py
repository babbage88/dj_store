from rest_framework import  serializers
from inventory.models import InventoryItem, InventoryCategory, InventoryItemType

class InventoryItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InventoryItem
        fields = [
            'name', 
            'display_name', 
            'sku', 
            'item_type', 
            'override_unit_price', 
            'description', 
            'quantity_in_stock', 
            'image_url',
            'is_active',
            'created_at',
            'updated_at'
            ]


class InventoryItemTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InventoryItemType
        fields = ['name', 'category', 'unit_price']

class InventoryCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InventoryCategory
        fields = ['name', 'display_name']
