from email import message
from random import choice, choices
from django.db import models
from django.urls import reverse
from .helper.models import TrackingModel
from django.conf import settings
from .options import ORDER_STATUS_CHOICES, ORDER_STATUS_PENDING, ORDER_STATUS_PENDING
from .utilis import generte_order_code
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})


class Product(TrackingModel):
    name = models.CharField(max_length=234)
    image = models.ImageField(upload_to='photos/product')
    hover_image = models.ImageField(upload_to='photos/product')
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = "Products"

    # def get_url(self):
    #     return reverse("store:product_detail", args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=230)
    message = models.TextField()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.name


class Post(TrackingModel):
    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='photos/blog')
    content = models.TextField()
    slug = models.SlugField(max_length=255)
    comment = models.ManyToManyField(
        'Comment',   blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title


class Order(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(
        max_length=100, choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_PENDING)
    order_number = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.customer)

    def save(self, *args, **kwargs):
        if self.order_number == "":
            code = generte_order_code()
            self.order_number = code
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)


class ShipingAddress(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.address
