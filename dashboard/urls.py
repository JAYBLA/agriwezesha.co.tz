from django.urls import path
from .views import *


app_name = 'dashboard'

urlpatterns = [    
    path('',dashboard, name='home'),

    #Jobs
    path('career/new/', create_job, name='create_job'),
    path('careers/', job_list, name='jobs'),
    path('careers/<int:job_id>/update/', update_job, name='update-job'),
    path('careers/<int:job_id>/', job_detail, name='job-detail'),
    path('careers/<int:job_id>/delete/', job_delete, name='delete-job'),

    #Projects
    path('projects/', projectlist,name='projectlist'),   
]