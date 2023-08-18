# from django import forms
# from .models import Profile

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model =  Profile
#         fields = ['id_number', 'first_name', 'last_name', 'email','course']
#         labels = {
#             'id_number' : 'ID Number',
#             'first_name' : 'First Name',
#             'last_name' : 'Last Name',
#             'email' : 'Email', 
#             'course' : 'Course',            
#         }

#         widgets = {
#            'id_number' : forms.NumberInput(attrs={'class': 'form-control'}), 
#            'first_name': forms.TextInput(attrs={'class': 'form-control'}), 
#            'last_name' : forms.TextInput(attrs={'class': 'form-control'}), 
#            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
#            'course' : forms.TextInput(attrs={'class': 'form-control'}),           
#         }