"""
URL configuration for doctorapp project.
"""

from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), # OpenAPI schema Se descarga un archivo JSON tipo OpenAPI
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # Swagger UI para visualizar y probar la API
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'), # Redoc UI alternativa para visualizar la API
]