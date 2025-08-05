from django.contrib import admin
from inventory.models import InventoryItem, InventoryCategory, InventoryItemType


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ("name", "display_name", "sku", "get_category", "get_unit_price", "quantity_in_stock", "is_active")
    list_filter = ("is_active", "item_type__category")
    search_fields = ("name", "display_name", "sku", "description")

    @admin.display(description="Category")
    def get_category(self, obj):
        return obj.category or "❌ Missing"

    @admin.display(description="Unit Price")
    def get_unit_price(self, obj):
        return obj.unit_price or "❌ Missing"


@admin.register(InventoryItemType)
class InventoryItemTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "unit_price")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(InventoryCategory)
class InventoryCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "display_name")
    search_fields = ("name", "display_name")
