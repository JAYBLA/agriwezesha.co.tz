from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home,name='site-home'),
    path('contact/', views.contact,name='contact'),
    path('ajax-contact/', views.process_contact, name='contact_post'),
    path('history/', views.history,name='history'),
    path('careers/', views.careers,name='careers'), 
    path('volunteer/', views.volunteer,name='volunteer'), 
    path('approach/', views.approach,name='approach'), 
    path('donate/', views.donate,name='donate'),
    path('expert-panelist/', views.expert_panelist,name='expert_panelist'),    
    path('get-connected-to-market/', views.get_connected_to_market,name='get_connected_to_market'),    
    path('get-expert/', views.get_expert,name='get_expert'),    
    path('resources/', views.resources,name='resources'),    
    path('statistics/', views.statistics,name='statistics'),        
    path('stories/', views.stories,name='stories'),    
    path('team/', views.team,name='team'),
    path('testimonials/', views.testimonials,name='testimonials'),  
    path('trainings/', views.trainings,name='trainings'),  
    path('vision-mission/', views.vision_mission,name='vision_mission'),      
]