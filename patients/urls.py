"""
URL configuration for patients app.
"""

from django.urls import path
from patients.views import ListPatientsView, DetailPatientView
#from patients.views import ListPatientsView, DetailPatientView, list_patients, detail_patient, ListPatientsWithListAPIView

urlpatterns = [
    path('api/', ListPatientsView.as_view()),
    path('api/patient/<int:pk>/', DetailPatientView.as_view()),
]