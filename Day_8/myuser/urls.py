from django.urls import path 
from .views import *

urlpatterns = [
    
path('signup/',signup, name='signup'),
path('saveuser/',saveuser, name='saveuser'),
path('login/',login, name='login'),
path('home/',home, name='home'),
path('loginvalidation/',loginvalidation, name='loginvalidation'),

]