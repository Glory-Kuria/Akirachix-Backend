from django.urls import path
from .views import ClassPeriodListAPIView

urlpatterns = [
    path('class-periods/', ClassPeriodListAPIView.as_view(), name='class-period-list'),
    
]