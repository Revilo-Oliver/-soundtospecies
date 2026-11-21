from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
def home(request):
    return render(request,'index.html')

def admin_home(request):
    return render(request,'admin_home.html')

def login(request):
    if request.method == 'POST':
        # support either 'username' or 'email' form field
        username = request.POST.get('username') or request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # simple UX: show a message; do not attempt to send email here
        return render(request, 'forgot_password.html', {'message': 'If an account with that email exists, instructions will be sent.'})
    return render(request, 'forgot_password.html')
def add_manage(request):
    return render(request,'add&manage.html')

def add(request):
    return render(request,'add.html')

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'admin_home.html')