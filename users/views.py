from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.
def user_login(request):
    # if request.user.is_authenticated:
    #         return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/posts')
        else:
            return render(request, 'login/login.html', {'error_message': 'Invalid username or password'})

    return render(request, 'login/login.html')

def registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        user_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        retype_password = request.POST.get('retype_password')

       
        if password == retype_password:
            
            if User.objects.filter(username=user_name).exists():
                messages.success(request, "User with this Username already exists.")
            elif User.objects.filter(username=email).exists():
                messages.success(request, "User with this email already exists.")
            else:
                # Create user and log in
                user = User.objects.create_user(username=user_name, first_name=first_name, email=email, password=password)
                user.save()
                authenticated_user = authenticate(request, username=first_name, password=password)
                login(request, user)
                return redirect('/posts') 
        else:
            messages.error(request, "Password and Retype Password do not match.")
    return render(request,'registration/registration.html')

def user_logout(request):
    logout(request)
    return redirect("/login")