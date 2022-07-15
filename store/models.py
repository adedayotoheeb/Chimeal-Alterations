from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=234)
    image = models.ImageField()
    hover_image = models.ImageField()
    description = models.TextField()
    