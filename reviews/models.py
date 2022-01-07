""" Models outlined for the Reviews app """
from django.db import models

from products.models import Product
from profiles.models import UserProfile


class Review(models.Model):
    """ Outlines the fields necessary for a review of a product """
    RATING_CHOICES = (
        (1, 1),
        (1.5, 1.5),
        (2, 2),
        (2.5, 2.5),
        (3, 3),
        (3.5, 3.5),
        (4, 4),
        (4.5, 4.5),
        (5, 5),
    )
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE,
                                related_name='reviews')
    review_title = models.CharField(max_length=254, null=True,
                                    blank=True)
    review_content = models.TextField()
    rating = models.DecimalField(choices=RATING_CHOICES,
                                 decimal_places=1, max_digits=3,
                                 blank=False)
    reviewer_name = models.ForeignKey(UserProfile,
                                      on_delete=models.SET_NULL,
                                      null=True, blank=True,
                                      related_name='reviews')
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review_title

    def save(self, *args, **kwargs):
        self.product.avg_rating()
        super().save(*args, **kwargs)
