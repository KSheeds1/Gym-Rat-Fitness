from django.contrib import admin
from . models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'description',
        'price',
        'rating',
        'image',
        'length_of_time',
        'training_styles',
        'workout_duration',
        'program_goals',
        'nutrition_plan_features',
    )
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

# Register your models here.
