from django.urls import path
from .views import *


app_name = 'dashboard'

urlpatterns = [
    #Posts
    path('',dashboard, name='home', ),
    # path('posts/', dashboard_post_list, name='posts'),
    # path('post/new/', create_post, name='create_post'),
    # path('post/<int:pk>/edit/',PostUpdateView.as_view(),name='edit_post'), 
    # path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='delete_post'),

    #Jobs
    path('career/new/', create_job, name='create_job'),
    path('careers/', job_list, name='jobs'),
]