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
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        data = User.objects.create_user(first_name = first_name, last_name = last_name, email = email, password = password1)
        data.save()
        return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate (username = username, password = password)

        if user is not None:
            auth.login(request.user)
            return render('home')        

    return render(request, 'login.html')