from django.shortcuts import render
from inventory.models import InventoryItem, InventoryCategory, InventoryItemType
from rest_framework import permissions, viewsets
from .serializers import InventoryItemTypeSerializer, InventoryItemSerializer, InventoryCategorySerializer


class InventoryItemSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class InventoryItemTypeSet(viewsets.ModelViewSet):
    queryset = InventoryItemType.objects.all()
    serializer_class = InventoryItemTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class InventoryCategorySet(viewsets.ModelViewSet):
    queryset = InventoryCategory.objects.all()
    serializer_class = InventoryCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
