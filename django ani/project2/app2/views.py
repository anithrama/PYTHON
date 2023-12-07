from django.shortcuts import render
# from django.http import HttpResponse
from .models import *
from .home import *

# Create your views here.

# def home(request):
#     return HttpResponse('hello world')
# def index(request):
#     return render(request,'home.html')
  
def home(request):
    return render(request,'base.html')

def add_item(request):
    d=studform()
    if request.method=='POST':
        d=studform(request.POST)
        if d.is_valid():
            d.save()
            return list(request)
    return render(request,'add.html',{'form':d})


def user_form2(request):
    if request.method=='POST':
        d=studform(request.POST)
        if d.is_valid():
            d.save()
            return list(request)
    return render(request,'form2.html')

def list(request):
    p=student.objects.all()
    return render(request,'list.html',{'d':p})

def edit_item(request,p):
    b=student.objects.get(pk=p)
    d=studform(instance=b)
    if request.method=='POST':
        d=studform(request.POST,instance=b)
        if d.is_valid():
           d.save()
           return list(request)
    return render(request,'edit.html',{'form':d})

def delete_item(request,p):
    b=student.objects.get(pk=p)
    b.delete()
    return list(request)

def form3(request):
    if request.method=='POST':
        name1=request.POST.get('n')
        roll=request.POST.get('r')
        place1=request.POST.get('p')
        data=student.objects.create(name=name1,rollno=roll,place=place1)
        data.save()
        return list(request)
    return render(request,'form3.html')
