from .models import InventoryCategory

def categories_processor(request):
    return {
        "categories": InventoryCategory.objects.all()
    }
