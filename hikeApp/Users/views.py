from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages


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
    return render(request, "Users/login.html")
