from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def shopping(request):
    template = loader.get_template('shopping.html')
    return HttpResponse(template.render())

# Create your views here.
