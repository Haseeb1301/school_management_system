from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User, auth

def home(request):    
    return render(request, 'home.html')

def signup (request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']       
        password1 = request.POST['psw']
        # password2 = request.POST['password2']

        data = User.objects.create_user(first_name = first_name, last_name = last_name, email = email, password = password1, username = username)
        data.save()
        return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')        

    return render(request, 'login.html')