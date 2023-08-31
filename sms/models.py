# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User

# class CustomUser(AbstractUser):
#     ACCOUNT_TYPE_CHOICES = (
#         ('admin', 'Admin'),
#         ('student', 'Student'),
#         ('teacher', 'Teacher')
#     )
#     account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)

# class CustomUser(AbstractUser):
#     is_student = models.BooleanField('student status', default=False)
#     is_teacher = models.BooleanField('teacher status', default=False)

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     id_number = models.CharField(max_length=50)
#     type = models.CharField(max_length=50)

#     def __str__(self):
#         return f'Full_Name: {self.user.first_name} {self.user.last_name}, {self.id_number}'    

