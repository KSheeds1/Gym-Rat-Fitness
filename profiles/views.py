"""
Views to access the profile, order history, and to edit the profile
"""
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from reviews.models import Review
from checkout.models import Order
from community.models import Post
from .models import UserProfile
from .forms import UserProfileForm
from .forms import EditProfileForm


@login_required
def profile(request):
    """ Display user profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    reviews = Review.objects.filter(reviewer_name=profile)
    posts = Post.objects.filter(user_profile=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'reviews': reviews,
        'posts': posts,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """ Return information on past orders """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
                  f'This is a past confirmation for order number '
                  f'{order_number}. A confirmation email was sent on the '
                  f'order date.'))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def edit_profile(request):
    """ To edit basic profile information """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES,
                               instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect(reverse('profile'))
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = EditProfileForm(instance=profile)

    template = 'profiles/edit_profile.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
