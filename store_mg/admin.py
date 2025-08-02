from django.contrib import admin
from .models import InventoryItem, InventoryCategory


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "category", "unit_price", "quantity_in_stock", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("name", "sku", "description")
    ordering = ("name",)


@admin.register(InventoryCategory)
class InventoryCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
