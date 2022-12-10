from django.db import models

# Create your models here.

class Bikes(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    cooling = models.CharField(max_length=100)