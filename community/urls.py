from django.urls import path
from . import views
from .views import PostListView


urlpatterns = [
    path('our_community/', views.our_community, name='our_community'),
    path('my_community/', PostListView.as_view(), name='my_community'),
    path('add_post/', views.add_post, name='add_post'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
]
