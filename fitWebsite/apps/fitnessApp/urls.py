from django.urls import path, re_path
from apps.fitnessApp import views

urlpatterns = [    
   path('', views.index, name='index'),
   path('workout', views.workout, name='workout'),
   path('diet', views.diet, name='diet'),
   path('survey',views.survey,name='survey'),
   path('thanks/<int:id>/', views.thanks, name='thanks'),
   path('select-recommendations/', views.select_recommendations, name='select_recommendations'),
   path('show-recommendations/', views.show_recommendations, name='show_recommendations'),
   
]