from django.shortcuts import render
from .models import Todo
# Create your views here.

def Homepage(request):
    obj = Todo.objects.all()
    return render(request,'pages/1page.html',{'obj':obj})

def Secondpage(request):
    return render(request,'pages/2pages.html')