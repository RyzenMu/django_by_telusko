from django.db import models


class Employee(models.Model):
    empid = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)