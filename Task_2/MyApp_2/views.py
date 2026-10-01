from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def template(request):
    template=loader.get_template('SISTec.html')
    return HttpResponse(template)