from django.urls import path
from . import views
from .views import PostListView


urlpatterns = [
    path('our_community/', views.our_community, name='our_community'),
    path('my_community/', PostListView.as_view(), name='my_community'),
]
