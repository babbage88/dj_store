from django.shortcuts import render
from inventory.models import InventoryItem, InventoryCategory, InventoryItemType
from rest_framework import permissions, viewsets
from api.serializers import InventoryItemTypeSerializer, InventoryItemSerializer, InventoryCategorySerializer


class InventoryItemSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all().order_by('updated_at')
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class InventoryItemTypeSet(viewsets.ModelViewSet):
    queryset = InventoryItemType.objects.all()
    serializer_class = InventoryItemTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class InventoryCategorySet(viewsets.ModelViewSet):
    queryset = InventoryCategory.objects.all()
    serializer_class = InventoryCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
