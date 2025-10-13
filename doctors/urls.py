"""
URL configuration doctors app
"""

from django.urls import path
from doctors.views import ListDoctorsView, DetailDoctorView

urlpatterns = [
    path('api/list_doctors/', ListDoctorsView.as_view()),
    path('api/detail_doctor/<int:pk>/', DetailDoctorView.as_view()),
]
