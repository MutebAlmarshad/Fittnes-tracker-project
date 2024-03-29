from django.urls import path, re_path
from apps.fitnessApp import views

urlpatterns = [    
   path('', views.index, name='index'),
   path('workout', views.workout, name='workout'),
   path('diet', views.diet, name='diet'),
]