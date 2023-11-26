from django.shortcuts import render

# Create your views here.

def nomesh(request):
    return render(request,'nomesh.html')

def timetable(request):
    return render(request,'timetable.html')

def description(request):
    return render(request,'description.html')