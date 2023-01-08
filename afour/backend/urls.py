from django.urls import path
from . import views


urlpatterns = [
    
    path('skillview', views.Skillview.as_view()),
    path('skillview/<str:pk>', views.Skillview.as_view()),
    path('team_csv', views.team_csv, name='team_csv'),

]
