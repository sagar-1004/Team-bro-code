from django.urls import path, include

from frontend import views
from .views import *
from rest_framework.routers import DefaultRouter



urlpatterns = [

    # path('', views.home, name="home"),
    path('viewskill', views.viewskill, name="viewskill"),
    path('deleteoneelement/', views.deleteoneskill, name="deleteoneelement"),
    path('viewoneskill/', views.viewoneskill, name="viewoneskill"),
    path('viewoneskill/', views.viewoneskill, name="viewoneskill"),
    path('putoneskill/', views.putoneskill, name="putoneskill"),
    path('delete/<str:uid>', delete, name='delete'),
    path('', views.index),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("dashboard", views.dashboard, name="dasshboard"),
    path("logout", views.logout_request, name="logout"),
    path("index", views.index, name="index"),
    path('add-skill',views.addskill,name="oneskill"),
    path("load-skill",views.load_skill,name="loadskill"),
    path('team',views.team,name='team'),
    path('team-list',views.team_list,name='teamlist'),
]  
