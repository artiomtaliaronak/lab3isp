from django.urls import path
from . import views

urlpatterns = [

    path('register', views.register),

    path('login', views.login),

    path('taskform', views.createTask),

    path('', views.home),

]