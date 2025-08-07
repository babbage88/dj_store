from rest_framework import routers
from .views import InventoryItemSet, InventoryItemTypeSet, InventoryCategorySet

router = routers.DefaultRouter()
router.register(r'items', InventoryItemSet)
router.register(r'item-types', InventoryItemTypeSet)
router.register(r'categories', InventoryCategorySet)

urlpatterns = router.urls
