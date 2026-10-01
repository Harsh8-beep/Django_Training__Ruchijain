from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def login_view(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def student_registration(request):
    return render(request, "studentragistrationform.html")