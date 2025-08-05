from django.shortcuts import get_object_or_404, render
from .models import InventoryCategory, InventoryItem


def home(request):
    categories = InventoryCategory.objects.order_by("name")
    featured_items = InventoryItem.objects.filter(is_active=True).exclude(image_url="").order_by("?")[:5]

    return render(request, "inventory/home.html", {
        "categories": categories,
        "featured_items": featured_items,
    })


def category_items(request, slug):
    category = get_object_or_404(InventoryCategory, name__iexact=slug)
    items = InventoryItem.objects.filter(
        item_type__category=category,
        is_active=True
    ).select_related("item_type")

    return render(request, "inventory/category_items.html", {
        "category": category,
        "items": items,
    })


def product_detail(request, pk):
    item = get_object_or_404(
        InventoryItem.objects.select_related("item_type__category"),
        pk=pk,
        is_active=True
    )
    return render(request, "inventory/product_detail.html", {
        "item": item
    })
