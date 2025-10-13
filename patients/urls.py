"""
URL configuration for patients app.
"""

from django.urls import path
from patients.views import ListPatientsView, DetailPatientView
from rest_framework.routers import DefaultRouter
from .viewsets import PatientViewSet

router = DefaultRouter()
router.register(r'list_patients', PatientViewSet, basename='patients')
urlpatterns = router.urls

urlpatterns = [
    path('api/', ListPatientsView.as_view()),
    path('api/patient/<int:pk>/', DetailPatientView.as_view()),
] + router.urls