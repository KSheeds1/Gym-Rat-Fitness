from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ Used by superusers to perform CRUD ops on products """

    class Meta:
        model = Product
        exclude = ('rating',)

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name())
                          for c in categories]

        placeholders = {
            'category': 'Category',
            'sku': 'SKU',
            'name': 'Name',
            'description': 'Description',
            'price': 'Price',
            'image': 'Image',
            'image_url': 'Image URL',
            'length_of_time': 'Length of time',
            'training_styles': 'Training Styles',
            'workout_duration': 'Workout Duration',
            'program_goals': 'Program Goals',
            'nutrition_plan_features': 'Nutrition Plan Features',
        }

        self.fields['category'].choices = friendly_names
        for field in self.fields:
            if field != 'image':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
