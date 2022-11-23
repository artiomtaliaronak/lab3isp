from django.shortcuts import render
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

            return HttpResponse('success')


    context = {'form':form}

    return render(request, 'createtask.html', context=context)


#CRUD-READ
def viewTasks(request):
    
    tasks = Task.objects.all()

    context = {'tasks': tasks}

    return render(request, 'viewtasks.html', context=context)



def register(request):

    return render(request, 'register.html')


def login(request):

    return render(request, 'login.html')

















