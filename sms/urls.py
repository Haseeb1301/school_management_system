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
   

    # path('student/', views.index, name='sindex'),
    # path('student/<int:id>', views.view_student, name='view_student'),
    # path('student/add/', views.add, name='add' ),
    # path('student/edit/<int:id>/', views.edit, name='edit'),
    # path('student/delete/<int:id>/', views.delete, name='delete'),
    # path('student/details/<int:id>/', views.details, name='details'),

    # path('teacher/', views.index, name='tindex'),
    # path('teacher/<int:id>', views.view_teachers, name='view_teacher'),
    # path('teacher/add/', views.add, name='add' ),    
    # path('teacher/edit/<int:id>/', views.edit, name='edit'),
    # path('teacher/delete/<int:id>/', views.delete, name='delete'),
    # path('teacher/details/<int:id>/', views.details, name='details'),
]
