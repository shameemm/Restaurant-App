from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    place = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    
