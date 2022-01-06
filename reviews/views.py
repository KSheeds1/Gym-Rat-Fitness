""" Views to add, edit, and delete a review of a product """
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.contrib import messages

from products.models import Product
from .models import UserProfile
from .forms import ReviewForm


def add_review(request, product_id):
    """
    A view to allow users to add a review to a specific product
    """

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.reviewer_name = UserProfile.objects.get(user=request.user)
            form.save()
            messages.success(request, 'Successfully reviewed \
                             {product.name}')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to post review to \
                           {product.name}. Please ensure the form \
                            is valid.')
    else:
        form = ReviewForm()
        messages.info(request, f'You are creating a review for '
                      f'{product.name}')

    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
