from django.db import models


class InventoryCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    display_name = models.TextField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.display_name and self.name: # Only set if target_field is not already set
            self.display_name = self.name
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Inventory Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name    


class InventoryItemType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(InventoryCategory, on_delete=models.PROTECT)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name



class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.TextField(max_length=200, blank=False)
    sku = models.CharField(max_length=32, unique=True)

    item_type = models.ForeignKey(
        InventoryItemType,
        on_delete=models.PROTECT,
        help_text="Item type determines category (required)"
    )

    override_unit_price = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True,
        help_text="Optional override for unit price"
    )

    description = models.TextField(blank=True)
    quantity_in_stock = models.PositiveIntegerField(default=0)
    image_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def unit_price(self):
        return self.override_unit_price if self.override_unit_price is not None else self.item_type.unit_price

    @property
    def category(self):
        return self.item_type.category

        return None
    
    def save(self, *args, **kwargs):
        if not self.item_type and self.override_unit_price:
            default_category, _ = InventoryCategory.objects.get_or_create(name=self.name)
            self.item_type = InventoryItemType.objects.create(
                name=f"AutoType-{self.name}",
                category=default_category,
                unit_price=self.override_unit_price
            )
        if not self.display_name and self.name: # Only set if target_field is not already set
            self.display_name = self.name
        super().save(*args, **kwargs)


