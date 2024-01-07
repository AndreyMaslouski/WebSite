from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .models import Pro


def index(request):
    task = Task.objects.order_by('-id')
    return render(request,'main/index.html',{'title':'Главная страница','tasks':'title'})


def about(request):
    pro = Pro.objects.all()
    return render(request,'main/about.html',{'title':'Основа','tasks':'Основание'})

def people(request):
    return render(request,'main/people.html')


def index(requst):
    return HttpResponse("<h5>World and People</h5>")

def about(requst):
    return HttpResponse("<h5>about</h5>")

def help(requst):
    return HttpResponse("<h5>help</h5>")

def create(request):
    return render(request, 'main/create.html')

def draw(request):
    return render(request, 'main/draw.html')






