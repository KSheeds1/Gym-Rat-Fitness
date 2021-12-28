from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Returns the correct subtotal amount per product """
    return price * quantity
