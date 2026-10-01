from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myuser.models import User
from django.urls import reverse
# Create your views here.

def home(request):
    return render(request,'home.html')
def signup(request):
    return render(request,'signup.html')

def saveuser(request):
     user1=User()
     u=User.objects.filter(username=request.POST['username'])
     if not u:
         user1.username=request.POST['username']
         user1.password=request.POST['password']
         user1.name=request.POST['name']
         user1.save()
         return HttpResponseRedirect(reverse('login'))
     else:
         return render(request,'signup.html',{'errormessage':'Username is Already Exists'})
             
    
def login(request):
    return render(request,'login.html')


def loginvalidation(request):
    try:
        user1=User.objects.get(
            username=request.POST['username'],
            password=request.POST['password']    
        )
        #--------------------Session Create-----------------
        request.session['username']=user1.username
        request.session['name']=user1.name
        return HttpResponseRedirect(reverse('home'))
    
    except User.DoesNotExist:
        return render(request,'login.html',{'erg':'Invalid username or password'})


def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('login'))