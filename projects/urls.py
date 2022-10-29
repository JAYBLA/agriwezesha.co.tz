from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    #path('upload', views.upload_images,name='upload_images'),
    path('project-list', views.projectlist,name='projectlist'),   
]