from django.urls import path
from . import views


urlpatterns = [
    path('our_community/', views.our_community, name='our_community'),
    path('my_community/', views.my_community, name='my_community'),
]
