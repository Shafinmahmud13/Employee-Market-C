from django.db import models

# Create your models here.
class Categories(models.Model):
    Categories_name = models.CharField(max_length=10)
    Categories_id = models.IntegerField(primary_key=True)