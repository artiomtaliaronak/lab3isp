from django.shortcuts import render
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm

# Create your views here.

def home(request):

    queryAllData = Task.objects.all()

    context = {'tasks': queryAllData}

    return render(request, 'index.html', context=context)


def createTask(request):

    form = TaskForm()
    
    context = {'form': form}

    return render(request, 'taskform.html', context=context)



def register(request):

    return render(request, 'register.html')


def login(request):

    return render(request, 'login.html')

















