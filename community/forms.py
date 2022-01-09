from django import forms
from .models import Comments, Post


class NewPostForm(forms.ModelForm):
    """ Fields required for a user to post """
    class Meta:
        model = Post
        fields = ['description', 'image']


class NewCommentForm(forms.ModelForm):
    """ Fields required for a user to comment on a post"""
    class Meta:
        model = Comments
        fields = ['comment']
