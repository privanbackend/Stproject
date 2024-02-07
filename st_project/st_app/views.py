from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def register(request):

    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')

        print(name,email,pass1)

        my_user=User.objects.create_user(name,email,pass1)
        my_user.save()

        return HttpResponse('hii')

    return render(request, 'register.html')

def loginuser(request):

    if request.method=='POST':
        name=request.POST.get('username')
        pass1=request.POST.get('password1')

        print(name,pass1)

        user=authenticate(request,username=name,password=pass1)


        if user is not None:
            login(request,user)
            return render(request,'home.html')
    
        else:
            return HttpResponse('')

    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')


