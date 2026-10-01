from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def testPaper(request):
    que = "Who Developed Python?"
    a = 'Guido Van Rossum'
    b = 'James Gosling'
    c = 'Dennis Ritchie'
    d = 'Bjarne Stroustrup'
    context = {'que': que, 'a': a, 'b': b, 'c': c, 'd': d}
    template = loader.get_template('testPaper.html')
    res = template.render(context,request)
    return HttpResponse(res)


def info(request):
    name = "Charlie"
    department = "AI&DS"
    age = '22'
    context = {'name': name, 'department': department, 'age': age}
    template = loader.get_template('info.html')
    res = template.render(context, request)
    return HttpResponse(res)


def sum(request):
    a = 10
    b = 20
    c = 30
    sum = a + b +c
    context = {'a': a, 'b': b, 'c': c, 'sum': sum}
    template = loader.get_template('addition.html')
    res = template.render(context, request)
    return HttpResponse(res)


def result(request):
    context = {'name': 'Charlie', 'marks': 10}
    return render(request, 'result.html', context)


def voting(request):
    context = {'name' : 'Charlie', 'country' : 'India', 'age' : 22}
    return render(request, 'voting.html', context)


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


