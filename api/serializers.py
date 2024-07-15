from rest_framework import serializers
from student.models import Students
from classperiod.models import ClassPeriod
from course.models import Course
# from class.models import Class



class StudentSerializers(serializers.ModelSerializer):
    class meta:
        model = Students
        fields = "__all__"

class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = '__all__'
        
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
        
# class ClassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Class
#         fields = '__all__'
        