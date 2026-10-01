from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def facebook(request):
    s='<h1>This is Facebook Page</h1>'
    return HttpResponse(s)

def instagram(request):
    s='<h1>This is Instagram Page</h1>'
    return HttpResponse(s)