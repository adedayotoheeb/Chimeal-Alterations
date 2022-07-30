from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('cart', views.cart, name='cart'),
    path('shop', views.shop, name='shop'),
    path('<slug:category_slug>/', views.shop, name='product_by_category')

]
