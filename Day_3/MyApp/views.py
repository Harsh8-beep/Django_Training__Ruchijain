from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    template = loader.get_template('Home.html')
    res=template.render()
    return HttpResponse(res)

def about(request):
    template = loader.get_template('About.html')
    res=template.render()
    return HttpResponse(res)
