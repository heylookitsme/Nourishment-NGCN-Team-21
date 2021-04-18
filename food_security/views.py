from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index.html')
    #return render(request, '/index.html')

def learn(request):
    return render(request, 'learn.html')

def resources(request):
    return render(request, 'resources.html')

def about(request):
    return render(request, 'about.html')
