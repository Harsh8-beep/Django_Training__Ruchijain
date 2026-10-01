from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    return render(request, 'main.html')

def sistec(request):
    return render(request, 'sistec.html')

def lnct(request):
    return render(request, 'lnct.html')

def oist(request):
    return render(request, 'oist.html')
