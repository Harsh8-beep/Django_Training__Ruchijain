from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.student_register, name='studentragister'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('predict/', views.predict, name='predict'),
]