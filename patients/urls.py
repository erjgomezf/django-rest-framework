"""
URL configuration for patients app.
"""

from django.urls import path
from patients.views import PatientListView, list_patients, detail_patient

urlpatterns = [
    path('', PatientListView.as_view()),
    path('api/list_patients/', list_patients),
    path('api/detail_patient/<int:pk>/', detail_patient),
]