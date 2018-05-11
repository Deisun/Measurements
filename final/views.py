from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def assignment3(request):
    return render(request, 'main/assignment3.html')


def assignment2(request):
    return render(request, 'main/assignment2.html')


def assignment5(request):
    return render(request, 'main/assignment5.py')

