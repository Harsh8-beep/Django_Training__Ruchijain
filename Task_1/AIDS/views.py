from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    s="<h1>About AI&DS Department</h1>\n<p>The AI&DS department is dedicated to providing comprehensive education and research in the field of Artificial Intelligence and Data Science.</p>"
    return HttpResponse(s)