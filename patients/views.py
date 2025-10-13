from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView

from .serializers import PatientSerializer
from .models import Patient


# Create your views here.
# GET /api/list_patients/ => lista pacientes
# POST /api/list_patients/ => crear paciente
# DELETE /api/list_patients/ => eliminar pacientes

class ListPatientsView(ListAPIView, CreateAPIView, DestroyAPIView):
    '''
    Vista basada en clase para listar todos los pacientes.
    * Atributos:
        - queryset: Conjunto de todos los objetos Patient.
        - serializer_class: Serializador a utilizar para Patient.
        - allowed_methods: Métodos HTTP permitidos (GET, POST, DELETE).
    * Métodos:
        - ListAPIView: Proporciona la funcionalidad para listar objetos.
        - CreateAPIView: Proporciona la funcionalidad para crear nuevos objetos.
        - DestroyAPIView: Proporciona la funcionalidad para eliminar objetos.
    '''
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    allowed_methods = ['GET', 'POST', 'DELETE']


# GET /api/patient/<int:pk>/ => detalle paciente
# PUT /api/patient/<int:pk>/ => actualizar paciente
# DELETE /api/patient/<int:pk>/ => eliminar paciente
class DetailPatientView(RetrieveUpdateDestroyAPIView):
    '''
    Vista para recuperar, actualizar o eliminar un paciente específico.
    * Atributos:
        - allowed_methods: Métodos HTTP permitidos (GET, PUT, DELETE).
        - serializer_class: Serializador a utilizar para Patient.
        - queryset: Conjunto de todos los objetos Patient.
        - lookup_field: Campo utilizado para buscar el paciente (por defecto es 'pk').
        - lookup_url_kwarg: Nombre del parámetro en la URL (por defecto es 'pk').
    * Métodos:
        - RetrieveUpdateDestroyAPIView: Proporciona la funcionalidad para recuperar, actualizar y eliminar objetos.
    '''
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    lookup_field = 'pk' # Campo utilizado para buscar el paciente (por defecto es 'pk')
    lookup_url_kwarg = 'pk' # Nombre del parámetro en la URL (por defecto es 'pk')


    """"""