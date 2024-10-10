from django.contrib.auth.models import User
from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='inventory_items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class InventoryChange(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    change_type = models.CharField(max_length=255)  # e.g., 'restock', 'sold'
    quantity_changed = models.IntegerField()
    changed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_changed = models.DateTimeField(auto_now_add=True)
