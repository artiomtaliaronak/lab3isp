from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    
    clientlist = [

        {
            'id':'1',
            'name':'Jonh Cena'
            
        },

        {
            'id':'2',
            'name':'Wazzup Beijing'

        }

    ]

    context = {'client': clientlist}

    return render(request, 'index.html', context)


def register(request):

    return render(request, 'register.html')


def login(request):

    return render(request, 'login.html')

















