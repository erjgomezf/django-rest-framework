"""
URL configuration doctors app
"""

from django.urls import path
from doctors.views import list_doctors, detail_doctor

urlpatterns = [
    path('api/list_doctors/', list_doctors, name='list_doctors'),
    path('api/detail_doctor/<int:pk>/', detail_doctor, name='detail_doctor'),
]
