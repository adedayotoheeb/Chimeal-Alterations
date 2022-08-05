from django.shortcuts import get_object_or_404, render
from .models import Order, Product, Category
from django.db.models import Q
from django.contrib.auth import get_user_model

# Create your views here.


def home(request):
    products = Product.objects.filter(is_available=True).order_by('-create_at')[:12]
    context = {
        'products': products
    }
    return render(request, 'store/index.html', context)

def shop(request, category_slug= None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.select_related('category').filter(is_available=True).order_by('-create_at')
    context = {
        'products': products,
        'product_count':product_count, 
    }
    return render(request, 'store/shop-fullwidth.html')

def blog(request):
    return render(request, 'store/blog-grid-view.html')


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.get_user_model()
        order,created = Order.objects.get_or_create(Q(customer=customer) & Q(order_status='Pending'))
    return render(request, 'store/cart.html')
