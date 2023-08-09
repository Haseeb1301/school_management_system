from django.urls import path
from . import views
app_name="teacher"
urlpatterns = [
    path('', views.index, name='tindex'),
    path('teacher', views.view_teachers, name='teacher'),
    path('add/', views.add, name='add' ),    
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('details/<int:id>/', views.details, name='details'),
]