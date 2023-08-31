from django.shortcuts import render

def course(request):
    return render(request, 'courses/subjects.html')

def attendance(request):
    return render(request, 'attendence.html')

