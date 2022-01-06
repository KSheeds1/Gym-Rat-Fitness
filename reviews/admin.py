""" Admin panel configuration for Reviews app """
from django.contrib import admin

from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Outlines the fields displayed in Admin panel for the Reviews app
    """
    model = Review
    list_display = (
        'product',
        'review_title',
        'reviewer_name',
        'rating',
        'review_date',
    )
    ordering = ('product',)


admin.site.register(Review, ReviewAdmin)
