from django.shortcuts import render


def about(request):
    return render(request, 'about.html')

def info(request):
    return render(request, 'info.html')

# Create your views here.
