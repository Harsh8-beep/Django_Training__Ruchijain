from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    s="<h1>Welcome to SISTec - Sagar Institute of Science and Technology</h1>\n<p>We are committed to providing quality education and fostering innovation.</p>"
    return HttpResponse(s)