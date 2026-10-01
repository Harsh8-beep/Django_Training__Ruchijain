from django.urls import path
from . import views

urlpatterns=[
        
    path('deleteEmployee/',views.deleteEmployee,name="deleteEmployee"),
    path('updateEmployee/',views.updateEmployee, name="updateEmployee"),
    path('employeelist/',views.employeelist,name="employeelist"),
    path('saveuser/',views.saveuser,name="saveuser"),
    path("", views.home, name="home"),
 ]