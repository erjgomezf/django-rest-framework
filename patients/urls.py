"""
URL configuration for patients app.
"""

from django.urls import path
from patients.views import ListPatientsView, DetailPatientView, list_patients, detail_patient, ListPatientsWithListAPIView

urlpatterns = [
    path('api/', ListPatientsView.as_view()),
    path('api/<int:pk>/', DetailPatientView.as_view()),
    path('api/patients/', ListPatientsWithListAPIView.as_view()),
    path('api/list_patients/', list_patients),
    path('api/detail_patient/<int:pk>/', detail_patient),
]