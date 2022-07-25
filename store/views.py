from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'store/index.html')


def blog(request):
    return render(request, 'store/blog-grid-view.html')

def cart(request):
    return render(request, 'store/cart.html')
