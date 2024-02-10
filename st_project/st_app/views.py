from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')

        # Check if username or email already exists
        existing_user = User.objects.filter(username=name).exists()
        existing_email = User.objects.filter(email=email).exists()

        if existing_user or existing_email:
            # If username or email already exists, display a message
            message = "Username or email is already in use."
            return render(request, 'register.html', {'message': message})

        # If username and email are not already in use, create the user
        my_user = User.objects.create_user(name, email, pass1)
        my_user.save()

        return render(request, 'login.html')

    return render(request, 'register.html')


def loginuser(request):

    if request.method=='POST':
        name=request.POST.get('username')
        pass1=request.POST.get('password1')

        user=authenticate(request,username=name,password=pass1)


        if user is not None:
            login(request,user)
            return redirect('home')
    
        else:
            message = "Invalid Credentials."
            return render(request, 'login.html', {'message': message})

    return render(request, 'login.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def signout(request):
    logout(request)
    return redirect('login')

def games(request):
    return render(request, 'games.html')


