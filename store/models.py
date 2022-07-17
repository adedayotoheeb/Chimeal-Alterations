from django.db import models
from django.urls import reverse
from .helper import TrackingModel

# Create your models here.


class Category(models.Model):
    named = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='photos/categories')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(TrackingModel):
    name = models.CharField(max_length=234)
    image = models.ImageField(upload_to='photos/product')
    hover_image = models.ImageField(upload_to='photos/product')
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    is_availabele  = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = "Products"

    # def get_url(self):
    #     return reverse("store:product_detail", args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name


class Blog(TrackingModel):   
    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='photos/blog')
    content = models.TextField()
    slug = models.SlugField(max_length=255) 

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title

class Comment(models.Model):
    pass