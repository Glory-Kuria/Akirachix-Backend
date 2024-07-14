from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import ClassPeriod
from .serializers import ClassPeriodSerializer

class ClassPeriodListAPIView(generics.ListAPIView):
    queryset = ClassPeriod.objects.all()
    serializer_class = ClassPeriodSerializer