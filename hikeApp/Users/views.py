from django.shortcuts import render

def signup(request):
    return render(request, 'Users/signup.html')

def login(request):
    return render(request, "Users/login.html")
