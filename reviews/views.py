""" Views to add, edit, and delete a review of a product """
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import UserProfile
from .forms import ReviewForm
from .models import Review


@login_required
def add_review(request, product_id):
    """
    A view to allow users to add a review to a specific product
    """
    product = get_object_or_404(Product, pk=product_id)
    if not request.user.is_authenticated:
        messages.info(request, 'You must be registered or logged in \
                      to create a review')
        return redirect('login')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.reviewer_name = UserProfile.objects.get(user=request.user)
            form.save()
            messages.success(request, f'Successfully reviewed '
                             f'{product.name}')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, f'Failed to post review to '
                           f'{product.name}. Please ensure the form '
                           f'is valid.')
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


@login_required
def edit_review(request, review_id):
    """ Allow user to edit a specific review that they created"""
    review = get_object_or_404(Review, pk=review_id)
    if review.reviewer_name != request.user.userprofile:
        messages.error(request, 'Sorry, you can only edit your \
                        own reviews')
        return redirect('profile')

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer_name = (
                UserProfile.objects.get(user=request.user))
            form.save()
            messages.success(request, 'Review updated')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Successfully updated review')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f"You are editing your review titled"
                      f": '{review.review_title}'")

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }
    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Allows users to delete a specific review """
    review = get_object_or_404(Review, pk=review_id)
    if review.reviewer_name.user == request.user:
        review.delete()
        messages.success(request, 'Your review has been deleted')
        return redirect('home')
    messages.error(request, 'Sorry, you can only delete your \
                   own reviews')
    return redirect(reverse('product_detail', args=[product.id]))