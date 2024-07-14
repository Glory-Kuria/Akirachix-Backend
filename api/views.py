from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Students
from .serializers import StudentSerializers

class StudentListView(APIView):
    def get(self,request):
        student= Students.objects.all()
        serializer =StudentSerializers(student,many=True)
        return Response(serializer.data) 
