from django.contrib import admin
from inventory.models import InventoryItem, InventoryCategory


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "category", "unit_price", "quantity_in_stock", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("name", "sku", "description")



@admin.register(InventoryCategory)
class InventoryCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "display_name")
    search_fields = ("name", "display_name")
