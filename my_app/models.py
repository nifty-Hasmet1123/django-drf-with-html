from django.db import models

# Create your models here.
class Owner(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)