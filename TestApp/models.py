from django.db import models

# Create your models here.
class Result(models.Model):
    values = models.CharField(max_length=100)
    result = models.CharField(max_length=30)

