from django.db import models

# Create your models here.
class Course(models.Model):
    course_name =models.CharField(max_length = 20)
    course_id = models.PositiveSmallIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    enrolment_capacity = models.PositiveSmallIntegerField()
    department_id =models.IntegerField()
    department = models.CharField(max_length=20)
    Syllabus = models.TextField()
    course_duration = models.IntegerField()
    
    
    def __str__(self):
          return f"{self.course_name} {self.course_code}"