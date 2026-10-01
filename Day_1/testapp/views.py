from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def charlie(request):
    s='<H1> Hello Charlie </H1>'
    return HttpResponse(s)
def dept(request):
    s='<H1> CSE-AI&DS </H1>'
    return HttpResponse(s)
def college(request):
    s='<H1> Sagar Institute of Science and Technology </H1>'
    return HttpResponse(s)

