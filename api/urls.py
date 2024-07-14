
from django.urls import path,include
from .views import StudentListView

urlpatterns = [
    path('api/', include('classperiod.urls')), 
    path("students/",StudentListView.as_view(),
         name = "student_list_view")
]

# urlpatterns = [
#     path("students/", StudentListView.as_view(), name="student_list_view")
# ]

# from django.urls import path
# from .views import StudentListView

# from django.contrib import admin
# from django.urls import path, include

