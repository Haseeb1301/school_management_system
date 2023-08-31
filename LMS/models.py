from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)                         
    subject = models.CharField(max_length=50)                               

class Enrollment(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.CharField(max_length=50)

class Attendance(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Assignment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    type = models.CharField(max_length=50) 


class Exams(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    type = models.CharField(max_length=50) 
