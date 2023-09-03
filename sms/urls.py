from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'), 
    path('home/', views.home_page, name='home'),
    
    path('student/', include("students.urls")),
    path('teacher/', include('teachers.urls')),
    
    path('courses/', views.course, name='course'),
    path('enrollment/', views.enrollment, name='enrollment'),
    path('assignments/', views.assignment, name='assignment'),
    path('addassignments/', views.add_assignment, name='add_assignment'),
    path('attendence/', views.attendence, name='attendence'),
    path('addattendence/', views.add_attendence, name='add_attendence'),
    path('exams/', views.exam, name='exam'),   
    path('addexams/', views.add_exam, name='add_exam'),
    path('grades/', views.grade, name='grades'),
    path('addgrades/', views.add_grade, name='add_grades'),    
   

    # path('student/', views.index, name='sindex'),
    # path('student/<int:id>', views.view_student, name='view_student'),
    # path('student/add/', views.add, name='add' ),
    path('student/edit/<int:id>/', views.edit, name='s_edit'),
    path('student/delete/<int:id>/', views.delete, name='s_delete'),
    path('student/details/<int:id>/', views.details, name='s_details'),

    # path('teacher/', views.index, name='tindex'),
    # path('teacher/<int:id>', views.view_teachers, name='view_teacher'),
    # path('teacher/add/', views.add, name='add' ),    
    # path('teacher/edit/<int:id>/', views.edit, name='edit'),
    path('teacher/delete/<int:id>/', views.delete, name='delete'),
    path('teacher/details/<int:id>/', views.details, name='details'),
]
