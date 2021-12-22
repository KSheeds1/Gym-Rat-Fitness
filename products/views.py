from django.shortcuts import render
from . models import Product


def get_products(request):
    """
    A view to show all products including sorting & search queries
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
