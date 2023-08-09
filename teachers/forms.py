from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model =  Teacher
        fields = ['teacher_number', 'first_name', 'last_name', 'email','course']
        labels = {
            'teacher_number' : 'Teacher Number',
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email' : 'Email', 
            'course' : 'Course',            
        }

        widgets = {
           'teacher_number' : forms.NumberInput(attrs={'class': 'form-control'}), 
           'first_name': forms.TextInput(attrs={'class': 'form-control'}), 
           'last_name' : forms.TextInput(attrs={'class': 'form-control'}), 
           'email' : forms.EmailInput(attrs={'class': 'form-control'}),
           'course' : forms.TextInput(attrs={'class': 'form-control'}),           
        }