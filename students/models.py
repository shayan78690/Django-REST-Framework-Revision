from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50, default='default_name')
    branch = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.name