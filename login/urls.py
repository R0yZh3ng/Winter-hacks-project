from django.contrib import admin
from django.urls import path, include
from . import views
from app import views as app_views


urlpatterns = [
    path('', views.home, name = "home"),
    path('signup/', views.signup, name = "signup"),
    path('loginPage/', views.loginPage, name = "loginPage"),
    path('chatroom/', views.chatroom, name = "chatroom"),
    path('polls/', views.polls, name = "polls"),
    path('logOut/', views.logOut, name = "logOut"),
    path('createP/', views.createP, name = "createP"),
    path('vote/poll_id', app_views.vote, name = "vote"),
    path('results/', app_views.results, name = "results"),

    

]
