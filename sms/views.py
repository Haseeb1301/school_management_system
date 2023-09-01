from django.http import HttpResponseRedirect, HttpResponse
from telnetlib import LOGOUT
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# from django.views import View
# from sms.forms import AdminSignUpForm, LoginForm
# from .forms import ProfileForm
from userprofile.models import Profile

from teachers.models import Teacher
from teachers.forms import TeacherForm

from students.models import Student
from students.forms import StudentForm

def course(request):
    return render(request, 'courses/subjects.html')

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
                return render(request, 'teachers/t_index.html', context={'type': user.profile.type})
            else:
                 return render(request, 'base.html')
        else:
             return HttpResponse("Username or Password is not correct")
    return render(request, 'login.html')



# ##### STUDENT VIEWS #######

def index(request):
    students = User.objects.filter(profile__type='student')    
    return render (request, 'students/s_index.html', { 'students' : students, 'current_user': request.user })

def view_student (request, id_number):
    student = User.objects.get(profile__id_number=id_number)
      
    return HttpResponseRedirect(reverse('sindex'))


def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_marks = form.cleaned_data['marks']

            new_student = Student (
                student_number = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                field_of_study = new_field_of_study,
                marks = new_marks, 
            )

            new_student.save()
            return render (request, 'students/s_add.html', {
                'form' : StudentForm(),
                'success' : True
            }) 
        else:
            form = StudentForm()
        return render(request, 'students/s_add.html', {
            'form' : StudentForm()
        })         
    return render(request , 'students/s_add.html')

def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/s_edit.html',{
                'form' : form,
                'success' : True
             })
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)
            return render(request, 'students/s_edit.html',{
                'form' : form,                
            })       
    return render(request , 'students/s_edit.html')

def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))

def details(request, id):
    student=Student.objects.get(pk=id)
    context={
        "student":student
    }
    return render(request, 'students/s_details.html',context)


# ######## VIEW TEACHERS ###############


def index(request):
    teachers = Teacher.objects.all()    
    return render (request, 'teachers/index.html', { 'teachers' : teachers })

def view_teachers (request):
    teacher = Teacher.objects.all()
    return HttpResponseRedirect(reverse('teachers:index'))


def add(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            new_teacher_number = form.cleaned_data['teacher_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_course = form.cleaned_data['course']            

            new_teacher = Teacher (
                teacher_number = new_teacher_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                course = new_course,                
            )

            new_teacher.save()
            return render (request, 'teachers/t_add.html', {
                'form' : TeacherForm(),
                'success' : True
            }) 
        else:
            form = TeacherForm()
        return render(request, 'teachers/t_add.html', {
            'form' : TeacherForm()
        })         
    return render(request , 'teachers/t_add.html')

def edit(request, id):
    if request.method == 'POST':
        teacher = Teacher.objects.get(pk=id)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return render(request, 'teachers/t_edit.html',{
                'form' : form,
                'success' : True
             })
        else:
            teacher = Teacher.objects.get(pk=id)
            form = TeacherForm(instance=teacher)
            return render(request, 'teachers/t_edit.html',{
                'form' : form,                
            })       
    return render(request , 'teachers/t_edit.html')

def delete(request, id):
    if request.method == 'POST':
        teacher = teacher.objects.get(pk=id)
        teacher.delete()
    return HttpResponseRedirect(reverse('index'))

def details(request, id):
    return render(request, 'teachers/t_details.html')

