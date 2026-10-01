from django.shortcuts import render
from django.http import HttpResponse
from database.models import Employee


# Create your views here.
def saveuser(request):    #create record ( C of CRUD)
    Eno = 4
    ename = "kaalua"
    esal = 10000
    emp = Employee(Eno=Eno,ename=ename,esal=esal)
    emp.save()
    return HttpResponse("<h1>user save Successfully</h1>")
def employeelist(request):           #read records (R of CRUD)
    Employees= Employee.objects.all()          # it return querry set of employee objectres
    res= render(request,'employeelist.html',{'Employees':Employees})
    return res
def updateEmployee(request):
    id = 5
    Eno = 105
    ename = "chapta"
    esal = 33000
    Employee(id=id,Eno=Eno, ename=ename,esal=esal).save()
    return HttpResponse("<h1>user updated Successfully</h1>")
def deleteEmployee(request):
    id=2
    emp=Employee.objects.filter(id=id)
    emp.delete()
    return HttpResponse("<h1>delete record Successfully</h1>")
def home(request):
    Employees = Employee.objects.all()
    return render(request, "employeelist.html", {"Employees": Employees})






    

