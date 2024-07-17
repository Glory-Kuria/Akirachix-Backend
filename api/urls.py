
from django.urls import path,include
from .views import StudentListView
from .views import ClassPeriodListView
from .views import CourseListView
from .views  import TeacherListView
from .views import ClassListView
# from .views import ClassListView

urlpatterns = [
    path("student/",StudentListView.as_view(),name="student_list_view"),
    path('class-periods/', ClassPeriodListView.as_view(), name='classperiod-list-view'),  
    path('course/', CourseListView.as_view(), name='course-list-view'),
    path('teacher/', TeacherListView.as_view(), name='teacher-list-view'),
    path('classroom/', ClassListView.as_view(),name='classroom-list-view'),
   
]
