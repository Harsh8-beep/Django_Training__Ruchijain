from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup, name="signup"),
    path("student-registration/", views.student_registration, name="student_registration"),
]