from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Students
from .serializers import StudentSerializers
from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from course.models import Course
from .serializers import CourseSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from classroom.models import Class
from .serializers import ClassSerializer





class StudentListView(APIView):
    def get(self,request):
        students= Students.objects.all()
        serializer =StudentSerializers(students,many=True)
        return Response(serializer.data) 

class ClassPeriodListView(APIView):
    def get (self,request):
        classperiods= ClassPeriod.objects.all()
        serializer =ClassPeriodSerializer(classperiods,many=True)
        return Response(serializer.data)
    
    
class CourseListView(APIView):
    def get (self,request):
        courses= Course.objects.all()
        serializer= Course(courses,many=True)
        return Response(serializer.data)
    
class TeacherListView(APIView):
    def get (self,request):
        teachers= Teacher.objects.all()
        serializer= Teacher(teachers,many=True)
        return Response(serializer.data)    
    
     
class ClassListView(APIView):
    def get (self,request):
        classes= Class.objects.all()
        serializer= Class(classes,many=True)
        return Response(serializer.data)
    