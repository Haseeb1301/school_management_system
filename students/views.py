from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

# from .models import Student

from django.contrib.auth.models import User
# from .forms import StudentForm

# Create your views here.

def index(request):
    students = User.objects.filter(profile__type='student')    
    return render (request, 'students/index.html', { 'students' : students, 'current_user': request.user })

def view_student (request, id_number):
    student = User.objects.get(profile__id_number=id_number)
    return   
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
            return render (request, 'students/add.html', {
                'form' : StudentForm(),
                'success' : True
            }) 
        else:
            form = StudentForm()
        return render(request, 'students/add.html', {
            'form' : StudentForm()
        })         
    return render(request , 'students/add.html')

def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html',{
                'form' : form,
                'success' : True
             })
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)
            return render(request, 'students/edit.html',{
                'form' : form,                
            })       
    return render(request , 'students/edit.html')

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
    return render(request, 'students/details.html',context)