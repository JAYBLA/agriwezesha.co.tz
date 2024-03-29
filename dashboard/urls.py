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
    path('projects/new/', create_project, name='create_project'),
    path('projects/<int:project_id>/', project_detail, name='project-detail'),
    path('projects/<int:p_id>/update/', update_project, name='update-project'),
    path('projects/<int:p_id>/delete/', project_delete, name='delete-project'),

    #Project_Images
    path('project-images/', images,name='images'),
    path('project-images/new/', project_images, name='add_images'),    
    path('project-images/<int:image_id>/delete/', project_photo_delete, name='delete-project-image'),
    
        #Agroforests
    path('agroforests/', agroforestlist,name='agroforestlist'),
    path('agroforests/new/', create_agroforest, name='create_agroforest'),
    path('agroforests/<int:project_id>/', agroforest_detail, name='agroforest-detail'),
    path('agroforests/<int:p_id>/update/', update_agroforest, name='update-agroforest'),
    path('agroforests/<int:p_id>/delete/', agroforest_delete, name='delete-agroforest'),     
]