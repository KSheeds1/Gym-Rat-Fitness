from django.urls import path
from . import views
from .views import PostListView, UserPostListView


urlpatterns = [
     path('our_community/', views.our_community, name='our_community'),
     path('my_community/', PostListView.as_view(), name='my_community'),
     path('add_post/', views.add_post, name='add_post'),
     path('<int:post_id>/', views.post_detail, name='post_detail'),
     path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
     path('delete_post/<int:post_id>/', views.delete_post,
          name='delete_post'),
     path('user/<int:user_id>', UserPostListView.as_view(),
          name='user_posts'),
]
