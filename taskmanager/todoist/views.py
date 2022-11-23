from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm

# Create your views here.

def home(request):

    return render(request, 'index.html')


#CRUD-CREATE
def createTask(request):

    form = TaskForm()
    
    if request.method == 'POST':
        
        form = TaskForm(request.POST)

        if form.is_valid():
            
            form.save()

            return redirect('viewtasks')


    context = {'form':form}

    return render(request, 'createtask.html', context=context)


#CRUD-READ
def viewTasks(request):
    
    tasks = Task.objects.all()

    context = {'tasks': tasks}

    return render(request, 'viewtasks.html', context=context)


#CRUD-UPDATE
def updateTask(request, pk):
    
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()

            return redirect('viewtasks')

    context = {'form':form}

    return render(request, 'updatetask.html', context=context)

#CRUD-DELETE
def deleteTask(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == 'POST':

        task.delete()

        return redirect('viewtasks')

    context = {'object': task}

    return render(request, 'deletetask.html', context=context)

    





def register(request):

    return render(request, 'register.html')


def login(request):

    return render(request, 'login.html')

















