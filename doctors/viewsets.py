from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import DoctorSerializer
from .models import Doctor
from .permissions import IsDoctor


# Create your views here.

class DoctorViewSet(viewsets.ModelViewSet):
    '''
    Vista basada en conjunto de vistas para el modelo Doctor.
    Proporciona operaciones CRUD completas para el modelo Doctor.
    * Atributos:
        - serializer_class: Serializador para el modelo Doctor.
        - queryset: Conjunto de todos los objetos Doctor.
    * Métodos:
        - set_on_vacation: Cambia el estado de vacaciones del doctor.
        - set_off_vacation: Cambia el estado de vacaciones del doctor.
    '''
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsDoctor]
    #permission_classes = [IsAuthenticatedOrReadOnly] # Permite solo a usuarios autenticados crear, actualizar o eliminar
    # permission_classes = [IsAuthenticated] # Permite solo a usuarios autenticados crear, actualizar o eliminar

    @action(["POST"], detail=True, url_path="set-on-vacation")
    def set_on_vacation(self, request, pk) -> Response:
        '''
        Cambia el estado de vacaciones del doctor.
        * Parámetros:
            -   request: Objeto de solicitud HTTP.
            -   pk: ID del doctor cuyo estado de vacaciones se va a cambiar.
        * Retorna:
            -   Response: Objeto de respuesta HTTP con el estado actualizado.
        '''
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"status": "El doctor está de vacaciones"})

    @action(["POST"], detail=True, url_path="set-off-vacation")
    def set_off_vacation(self, request, pk) -> Response:
        '''
        Cambia el estado de vacaciones del doctor.
        * Parámetros:
            -   request: Objeto de solicitud HTTP.
            -   pk: ID del doctor cuyo estado de vacaciones se va a cambiar.
        * Retorna:
            -   Response: Objeto de respuesta HTTP con el estado actualizado.
        '''
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"status": "El doctor ya no está de vacaciones"})