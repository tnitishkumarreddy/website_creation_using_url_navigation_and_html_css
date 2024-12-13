from django.shortcuts import render

# Create your views here.

def jspiders(request):
    return render(request,'jspiders.html')

def python(request):
    return render(request,'python.html')

def java(request):
    return render(request,'java.html')

def mern(request):
    return render(request,'mern.html')

def devops(request):
    return render(request,'devops.html')

def trainers(request):
    return render(request,'trainers.html')

def pdetails(request):
    return render(request,'pdetails.html')

def jdetails(request):
    return render(request,'jdetails.html')

def mdetails(request):
    return render(request,'mdetails.html')

def ddetails(request):
    return render(request,'ddetails.html')