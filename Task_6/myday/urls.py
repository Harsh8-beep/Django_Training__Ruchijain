from django.urls import path
from . views import *

urlpatterns = [
    path('productlist/',productlist, name='productlist'),
    path('createProduct/', createProduct, name='productlist'),
]