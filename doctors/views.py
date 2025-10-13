from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView

from .serializers import DoctorSerializer
from .models import Doctor

# Create your views here.
class ListDoctorsView(ListAPIView, CreateAPIView, DestroyAPIView):
    '''
    Vista basada en clase para listar todos los doctores.
    * Atributos:
        - queryset: Conjunto de todos los objetos Doctor.
        - serializer_class: Serializador a utilizar para Doctor.
        - allowed_methods: Métodos HTTP permitidos (GET, POST, DELETE).
    * Métodos:
        - ListAPIView: Proporciona la funcionalidad para listar objetos.
        - CreateAPIView: Proporciona la funcionalidad para crear nuevos objetos.
        - DestroyAPIView: Proporciona la funcionalidad para eliminar objetos.
    '''
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    allowed_methods = ['GET', 'POST', 'DELETE']

class DetailDoctorView(RetrieveUpdateDestroyAPIView):
    '''
    Vista para recuperar, actualizar o eliminar un doctor específico.
    * Atributos:
        - allowed_methods: Métodos HTTP permitidos (GET, PUT, DELETE).
        - serializer_class: Serializador a utilizar para Doctor.
        - queryset: Conjunto de todos los objetos Doctor.
        - lookup_field: Campo utilizado para buscar el doctor (por defecto es 'pk').
        - lookup_url_kwarg: Nombre del parámetro en la URL (por defecto es 'pk').
    * Métodos:
        - RetrieveUpdateDestroyAPIView: Proporciona la funcionalidad para recuperar, actualizar y eliminar objetos.
    '''
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    allowed_methods = ['GET', 'PUT', 'DELETE']
    lookup_field = 'pk' # Campo utilizado para buscar el doctor (por defecto es 'pk')
    lookup_url_kwarg = 'pk' # Nombre del parámetro en la URL (por defecto es 'pk')
