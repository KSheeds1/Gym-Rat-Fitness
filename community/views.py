""" Views for Review app """
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from profiles.models import UserProfile
from .forms import NewPostForm
from .models import Post, Comments, Like


def our_community(request):
    """ Renders the 'our community' page """

    return render(request, 'community/our_community.html')


class PostListView(ListView):
    """ Generate listview of the posts """

    model = Post
    template_name = 'community/my_community.html'
    context_object_name = 'posts'
    ordering = ['-posted_on']
    paginate_by = 10
    form_class = NewPostForm

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        form = self.form_class(self.request.POST or None)
        context['form'] = form
        return context


@login_required
def add_post(request):
    """ View to create a post """

    user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_profile = user
            post.save()
            messages.success(request, 'Post Added')
            return redirect('my_community')
        else:
            messages.error(request, 'Post failed. Please ensure \
                           your post is valid')
    else:
        form = NewPostForm()

    template = 'community/my_community.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def post_detail(request, post_id):
    """ View to render a specific post """

    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'community/post_detail.html', context)


@login_required
def edit_post(request, post_id):
    """ View for user to edit their posts """

    post = get_object_or_404(Post, pk=post_id)
    user = get_object_or_404(UserProfile, user=request.user)

    if not user == post.user_profile:
        messages.error(request, 'Sorry only the post owner can \
                       edit their posts')
        return redirect(reverse('my_community'))

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post edited successfully')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to edit your post. \
                           Please ensure the form is valid.')
    else:
        form = NewPostForm(instance=post)
        messages.info(request, 'You are editing on of your older \
                      posts.')

    template = 'community/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }
    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """ View for user to delete their own posts """

    post = get_object_or_404(Post, pk=post_id)
    user = get_object_or_404(UserProfile, user=request.user)

    if not user == post.user_profile:
        messages.error(request, 'Sorry only the post owner can \
                       delete their posts')

    post.delete()
    messages.success(request, 'Post deleted')
    return redirect(reverse('my_community'))