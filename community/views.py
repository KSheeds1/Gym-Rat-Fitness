from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import NewPostForm, NewCommentForm
from .models import Post, Comments, Like


def our_community(request):
    """ Renders the 'our community' page """

    return render(request, 'community/our_community.html')


class PostListView(ListView):
    """ Generate listview of the posts"""
    model = Post
    template_name = 'community/my_community.html'
    context_object_name = 'posts'
    ordering = ['-posted_on']
    paginate_by = 10
