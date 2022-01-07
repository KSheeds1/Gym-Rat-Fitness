""" The form used to add or edit a review of a product """
from django import forms

from . models import Review


class ReviewForm(forms.ModelForm):
    """
    Allows registered users to review and rate a specific product
    """

    class Meta:
        model = Review
        exclude = (
            'product',
            'reviewer_name',
            'review_date',
        )

    rating = forms.DecimalField(
        label='Rating',
        widget=forms.NumberInput(
            attrs={'step': 0.5, 'min': 1.0, 'max': 5.0}
        ),
    )
