from django.db import models

# Create your models here.

class Destinations(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    boole = models.BooleanField(default=False)
