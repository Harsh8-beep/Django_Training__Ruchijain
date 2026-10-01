from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    s="<h1>About CSE Department</h1>\n<p>The Computer Science and Engineering department is dedicated to providing cutting-edge education in the field of computer science.</p>"
    return HttpResponse(s)