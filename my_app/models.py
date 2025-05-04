from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from my_app.helpers import generate_unique_id
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Department(models.Model):
    department_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # uuid
    department = models.CharField(max_length=50, null=True) # IT or Finance etc should be pre existing 
    
    def __str__(self):
        return self.department
    
class Asset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset_id = models.CharField(max_length=100, unique=True, editable=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="assets", null=True) # by default this will always refer to the primary ID of the table
    item_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=30, null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    purchased_date = models.DateField(null=True, blank=True)
    
    # User tracking fields
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="assets_created")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="assets_updated")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.item_name
    
    def save(self, *args, **kwargs):
        if not self.asset_id:
            self.asset_id_modification()
        
        super().save(*args, **kwargs)
    
    def asset_id_modification(self):
        # trigger .full_clean from the Model class. It will then call the our custom clean method
        self.full_clean()
        
        if not self.asset_id:
            self.asset_id = generate_unique_id(Asset, "asset_id", "AST")
            
    def clean(self):
        # Check for existing item name (excluding self to allow updates)
        if Asset.objects.exclude(pk=self.pk).filter(item_name=self.item_name).exists():
            raise ValidationError({"item_code": "Item name already existing on the database."})
