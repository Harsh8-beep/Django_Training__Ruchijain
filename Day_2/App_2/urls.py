from django.urls import path
from App_2 import views

urlpatterns = [
    path('facebook/',views.facebook),
    path('instagram/',views.instagram),
]   