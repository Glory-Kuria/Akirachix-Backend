from django.db import models

# Create your models here.
class Students(models.Model):
    first_name= models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email=models.EmailField()
    date_of_birth = models.DateField()
    Code = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=28)
    
    def __str__(self):
     return f"{self.first_name}{self.last_name}"
    