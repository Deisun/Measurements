from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def assignment1(request):
    return render(request, 'main/assignment1.html')

def assignment2(request):
    return render(request, 'main/assignment2.html')

def assignment5(request):
    return render(request, 'main/weather.py')

