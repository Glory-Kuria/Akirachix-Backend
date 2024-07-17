from django.db import models
from teacher.models import Teacher
from course.models import Course
from student.models import Students
# Create your models here.
class Class(models.Model):
    class_name= models.CharField(max_length=20)
    section = models.CharField(max_length=20)
    teacher=models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,related_name='courses')
    students = models.ManyToManyField(Students)
    Course= models.ForeignKey(Course,on_delete=models.CASCADE)
    class_number = models.CharField(max_length=10)
    
    def __str__(self):
     return f"{self.class_name}"
 
 
    