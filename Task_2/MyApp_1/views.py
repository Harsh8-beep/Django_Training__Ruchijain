from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def testPaper(request):
    template = loader.get_template('testPaper.html')
    return HttpResponse(template.render())