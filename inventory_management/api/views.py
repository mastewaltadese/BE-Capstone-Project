# api/views.py
from rest_framework import viewsets, permissions
from .models import InventoryItem, InventoryChange
from .serializers import UserSerializer, InventoryItemSerializer, InventoryChangeSerializer
from django.contrib.auth.models import User

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return []  # Allow anyone to create a user
        return [permissions.IsAuthenticated()]  # Require authentication for other actions

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return InventoryItem.objects.filter(user=self.request.user)

class InventoryChangeViewSet(viewsets.ModelViewSet):
    queryset = InventoryChange.objects.all()
    serializer_class = InventoryChangeSerializer
    permission_classes = [permissions.IsAuthenticated]
