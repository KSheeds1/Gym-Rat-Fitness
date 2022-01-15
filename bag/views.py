from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view to render the shopping bag content page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add a quantity of the specified product to
    the shopping bag
    """

    product = get_object_or_404(Product, pk=item_id)
    if 'selected_price' in request.POST:
        price = request.POST['selected_price']
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, (f'Updated {product.name} '
                                f'quantity to {bag[item_id]}'))
    else:
        bag[item_id] = quantity
        messages.success(request, (f'Added {product.name} to your '
                                f'bag'))

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of a specified product in
    the shopping bag
    """

    product = get_object_or_404(Product, pk=item_id)
    if 'selected_price' in request.POST:
        price = request.POST['selected_price']
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, (f'Updated {product.name} '
                                   f'quantity to {bag[item_id]}'))
    else:
        bag.pop(item_id)
        messages.success(request, (f'Removed {product.name} from '
                                   f'your bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Remove item from the shopping bag
    """
    product = get_object_or_404(Product, pk=item_id)

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} '
                                  f'from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
