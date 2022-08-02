from django.contrib import admin
from . import models
from django.utils.http import urlencode
from django.utils.html import format_html
from django.urls import reverse
from django.db.models import Count

# Register your models here.stock


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock',
                    'category', 'is_available', 'inventory_status']
    list_editable = ['price']
    prepopulated_fields = {'slug': ['name']}
    list_per_page: int = 10
    list_select_related = ['category']
    search_fields = ['name__istartswith', 'price', 'category__istartswith']

    @admin.display(ordering='stock')
    def inventory_status(self, product: models.Product):
        if product.stock < 10:
            return "Low"
        return 'OK'


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_count']
    prepopulated_fields = {'slug': ['name']}
    list_per_page: int = 10

    def product_count(self, category):
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'category__id': str(category.id)
            })
        )
        return format_html('<a href="{}">{}</a>', url, category.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )


@admin.register(models.ShipingAddress)
class ShippigAddressAdmin(admin.ModelAdmin):
    list_display = ['order', 'customer', 'address']
    list_per_page: int = 10


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product',
                    'date_ordered', 'order_status', 'order_number']
    list_editable = ['order_status']


@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


# @admin.register(models.Ord)
# class OrderItemAdmin(admin.ModelAdmin):
#     pass
