from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse

from .models import Teacher
from .forms import TeacherForm

# Create your views here.

def index(request):
    teachers = Teacher.objects.all()    
    return render (request, 'teachers/t_index.html', { 'teachers' : teachers })

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
        teacher = Teacher.objects.get(pk=id)
        print(teacher.id)
        teacher.delete()
    return HttpResponseRedirect(reverse('teacher:tindex'))

def details(request, id):
    return render(request, 'teachers/t_details.html')
