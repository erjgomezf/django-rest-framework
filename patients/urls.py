"""
URL configuration for patients app.
"""

from django.urls import path
from patients.views import ListPatientsView, DetailPatientView

urlpatterns = [
    path('api/list_patients/', ListPatientsView.as_view()),
    path('api/patient/<int:pk>/', DetailPatientView.as_view()),
]