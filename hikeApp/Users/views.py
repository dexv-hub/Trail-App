from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'Users/signup.html', {'form': form})

def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('home')

    return render(request, "Users/login.html")

def logout(request):
    auth.logout(request)
    return redirect('home')

def profile(request):
    return render(request, 'Users/profile.html')
