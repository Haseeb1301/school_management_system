# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
# from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# from .models import Profile
# from .forms import ProfileForm

def home_page (request):       
    return render(request, 'home.html')

def signup_page (request):
    if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            uname = request.POST.get('username')
            email = request.POST.get('email')            
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')

            if pass1 != pass2:
                 return HttpResponse("Your passwords didnot Match!!!")
            else:
                my_user = User.objects.create_user(first_name = first_name, last_name= last_name, username = uname, email = email, password = pass1)
                my_user.save()             
    
            return redirect('login')
    return render(request, 'signup.html')

def login_page (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username = username, password = pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
             return HttpResponse("Username or Password is not correct")
    return render(request, 'login.html')


######## STUDENT VIEW ###########

# def index(request):
#     students = Profile.objects.all()    
#     return render (request, 'students/index.html', { 'students' : students })

# def view_student (request, id):
#     students = Profile.objects.get(pk=id)
#     return HttpResponseRedirect(reverse('sindex'))


# def add(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             new_student_number = form.cleaned_data['id_number']
#             new_first_name = form.cleaned_data['first_name']
#             new_last_name = form.cleaned_data['last_name']
#             new_email = form.cleaned_data['email']
#             new_course = form.cleaned_data['course']            

#             new_student = Student (
#                 student_number = new_student_number,
#                 first_name = new_first_name,
#                 last_name = new_last_name,
#                 email = new_email,
#                 field_of_study = new_field_of_study,
#                 marks = new_marks, 
#             )

#             new_student.save()
#             return render (request, 'students/add.html', {
#                 'form' : StudentForm(),
#                 'success' : True
#             }) 
#         else:
#             form = StudentForm()
#         return render(request, 'students/add.html', {
#             'form' : StudentForm()
#         })         
#     return render(request , 'students/add.html')

# def edit(request, id):
#     if request.method == 'POST':
#         student = Student.objects.get(pk=id)
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return render(request, 'students/edit.html',{
#                 'form' : form,
#                 'success' : True
#              })
#         else:
#             student = Student.objects.get(pk=id)
#             form = StudentForm(instance=student)
#             return render(request, 'students/edit.html',{
#                 'form' : form,                
#             })       
#     return render(request , 'students/edit.html')

# def delete(request, id):
#     if request.method == 'POST':
#         student = Student.objects.get(pk=id)
#         student.delete()
#     return HttpResponseRedirect(reverse('index'))

# def details(request, id):
#     student=Student.objects.get(pk=id)
#     context={
#         "student":student
#     }
#     return render(request, 'students/details.html',context)