from django.urls import path
from . import views

app_name="student"

urlpatterns = [
    path('', views.index, name='sindex'),
    path('<str:id_number>', views.view_student, name='view_student'),
    path('add/', views.add, name='add' ),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('details/<int:id>/', views.details, name='details'),
]