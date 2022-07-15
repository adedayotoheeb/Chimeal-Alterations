from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'store/index.html')


def blog(request):
    return render(request, 'store/blog-article.html')
