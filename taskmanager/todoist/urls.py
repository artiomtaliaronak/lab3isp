from django.urls import path
from . import views

urlpatterns = [

    path('register', views.register),

    path('login', views.login),

    

    path('', views.home),


    #CRUD

    path('createtask', views.createTask),

    path('viewtasks', views.viewTasks),

    #path('readtasks', views.viewTasks),

]