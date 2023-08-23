# from django import forms
# from .models import CustomUser, Profile

# class AdminSignUpForm(forms.ModelForm):
#     # Define the form fields for the admin sign-up form
#     account_type = forms.CharField(max_length=20, widget=forms.HiddenInput(), initial='admin')
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     email = forms.EmailField()
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(max_length=128, widget=forms.PasswordInput())

#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'last_name', 'email', 'username', 'password']
        
# class StudentSignUpForm(forms.ModelForm):
#     # Define the form fields for the student sign-up form
#     account_type = forms.CharField(max_length=20, widget=forms.HiddenInput(), initial='student')
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     email = forms.EmailField()
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(max_length=128, widget=forms.PasswordInput())

#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'last_name', 'email', 'username', 'password']
        
# class TeacherSignUpForm(forms.ModelForm):
#     # Define the form fields for the teacher sign-up form
#     account_type = forms.CharField(max_length=20, widget=forms.HiddenInput(), initial='teacher')
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     email = forms.EmailField()
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(max_length=128, widget=forms.PasswordInput())

#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'last_name', 'email', 'username', 'password']
        
# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(max_length=128, widget=forms.PasswordInput())

# 



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