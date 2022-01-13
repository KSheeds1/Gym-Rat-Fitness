from django import forms
from .widgets import CustomClearableFileInput
from .models import Post, Comments


class NewPostForm(forms.ModelForm):
    """ Fields required for a user to post """
    class Meta:
        model = Post
        fields = ['description', 'image', ]

    description = forms.CharField(label='Add a Post')
    image = forms.ImageField(label="", required=False,
                             widget=CustomClearableFileInput)


class NewCommentForm(forms.ModelForm):
    """ Fields required for a user to comment on a post"""

    class Meta:
        model = Comments
        fields = ['comment', ]

    comment = forms.CharField(label='Add comment')
