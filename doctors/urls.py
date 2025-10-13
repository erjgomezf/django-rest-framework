"""
URL configuration doctors app
"""

from django.urls import path
from doctors.views import ListDoctorsView, DetailDoctorView
from rest_framework.routers import DefaultRouter
from .viewsets import DoctorViewSet


router = DefaultRouter()
router.register(r"list_doctors", DoctorViewSet, basename="doctors")


urlpatterns = router.urls