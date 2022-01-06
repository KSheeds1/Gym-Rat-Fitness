from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True,
                                     blank=True)
    image_url = models.URLField(max_length=1024, null=True,
                                blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sub_price = models.DecimalField(max_digits=6, decimal_places=2,
                                    null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True,
                                blank=True)
    image = models.ImageField(null=True, blank=True)
    length_of_time = models.CharField(max_length=254, null=True,
                                      blank=True)
    training_styles = models.CharField(max_length=254, null=True,
                                       blank=True)
    workout_duration = models.CharField(max_length=254, null=True,
                                        blank=True)
    program_goals = models.CharField(max_length=254, null=True,
                                     blank=True)
    nutrition_plan_features = models.CharField(max_length=254,
                                               null=True, blank=True)

    def __str__(self):
        return self.name
