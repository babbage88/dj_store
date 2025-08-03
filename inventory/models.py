from django.db import models


class InventoryCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Inventory Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=32, unique=True, help_text="Unique stock keeping unit or barcode")
    category = models.ForeignKey(
        InventoryCategory,
        on_delete=models.PROTECT,
        help_text="Product category"
    )
    description = models.TextField(blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField(default=0)
    image_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["sku"]),
            models.Index(fields=["category"]),
        ]
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(fields=["name", "category"], name="unique_item_per_category"),
        ]

    def __str__(self):
        return f"{self.name} ({self.category})"
