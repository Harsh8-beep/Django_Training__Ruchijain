from django.shortcuts import render
from django.http import  HttpResponseRedirect
from database.models import Employee
from django.urls import reverse

def newEmployeeForm(request):
    res = render(request, 'newEmployeeForm.html')
    return res

def saveuser(request): #create
    e_no = request.POST['e_no']
    e_name = request.POST['e_name']
    e_sal = request.POST['e_sal']
    emp = Employee(e_no=e_no, e_name=e_name, e_sal=e_sal)
    emp.save()
    url=reverse('employeelist')
    return HttpResponseRedirect(url)

def employeelist(request):         # read Records (R of CRUD)
    Employees = Employee.objects.all()
    res = render(request, 'employeelist.html', {'Employees':Employees})
    return res

def updateEmployeeForm(request):
    id = request.GET['id']
    employee=Employee.objects.filter(id=id).values()
    res = render(request, 'updateEmployeeForm.html', {'employee':employee[0]})
    return res

def updateEmployee(request):
    id = request.POST['id']
    e_no = request.POST['e_no']
    e_name = request.POST['e_name']
    e_sal = request.POST['e_sal']
    Employee(id=id,e_no=e_no,e_name=e_name,e_sal=e_sal).save()
    url=reverse('employeelist')
    return HttpResponseRedirect(url)

def deleteEmployee(request):
    id = 3
    emp = Employee.objects.filter(id=id)
    emp.delete()
    return HttpResponseRedirect("<h1>User Delete Successfully</h1>")


# Create your views here.

