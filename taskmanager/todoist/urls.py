from django.urls import path
from . import views

urlpatterns = [

    path('register', views.register),

    path('login', views.login),

    

    path('', views.home),


    #CRUD

    path('createtask', views.createTask, name='createtask'),

    path('viewtasks', views.viewTasks, name='viewtasks'),

    path('updatetask/<str:pk>/', views.updateTask, name='updatetask'),

    path('deletetask/<str:pk>/', views.deleteTask, name='deletetask'),

    #path('readtasks', views.viewTasks),

]