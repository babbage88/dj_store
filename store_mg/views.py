from django.shortcuts import render
from .models import InventoryCategory, InventoryItem


def home(request):
    categories = InventoryCategory.objects.order_by("name")
    featured_items = InventoryItem.objects.filter(is_active=True).exclude(image_url="").order_by("?")[:5]

    return render(request, "inventory/home.html", {
        "categories": categories,
        "featured_items": featured_items,
    })
