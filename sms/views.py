# from django.http import HttpResponseRedirect
from telnetlib import LOGOUT
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views import View

# from sms.sms.forms import AdminSignUpForm, LoginForm

# from .models import Profile
# from .forms import ProfileForm

from userprofile.models import Profile

def home_page (request):       
    return render(request, 'home.html')

def signup_page (request):
    if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            uname = request.POST.get('username')
            email = request.POST.get('email',)            
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')
            type = request.POST.get('type')

            if pass1 != pass2:
                 return HttpResponse("Your passwords didnot Match!!!")
            else:
                my_user = User.objects.create_user(first_name = first_name, last_name= last_name, username = uname, email = email, password = pass1)
                my_user.save()

                profile = Profile(user=my_user, id_number=f'{type[:1].upper()}{my_user.id}', type=type)
                profile.save()
    
            return redirect('login')
    return render(request, 'signup.html')

def login_page (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username = username, password = pass1)
        if user is not None:
            login(request, user)
            if user.profile.type == 'student':
                 return redirect(reverse('student:sindex'))
            elif user.profile.type == 'teacher':
                return render(request, 'home.html', context={'type': user.profile.type})
        else:
             return HttpResponse("Username or Password is not correct")
    return render(request, 'login.html')

