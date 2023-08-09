from django.db import models

# Create your models here.

class Teacher(models.Model):
    teacher_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    course = models.CharField(max_length=50)  

    def __str__(self):
        return f'Teacher: {self.first_name} {self.last_name}'