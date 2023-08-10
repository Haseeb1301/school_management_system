from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User, auth

def index(request):    
    return render(request , 'home.html')

def SignUp (request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']       
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        data = User.objects.create_user(first_name = first_name,
                                        last_name = last_name,
                                        email = email,                                        
                                        password = password1)
        data.save()
    return render(request , 'signup.html')