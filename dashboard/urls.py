from django.urls import path
from .views import *


app_name = 'dashboard'

urlpatterns = [
    path('',dashboard, name='dashboard', ),
    path('posts/', dashboard_post_list, name='posts'),
    path('post/new/', create_post, name='create_post'),
    path('post/<int:pk>/edit/',PostUpdateView.as_view(),name='edit_post'), 
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='delete_post'),
]