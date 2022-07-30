from store.models import Category


def category_context(request):
    cat = Category.objects.all()
    return dict(category=cat)
