from django.db import models
 

class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    marks = models.FloatField(max_length=50)

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'