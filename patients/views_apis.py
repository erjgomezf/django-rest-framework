from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from .serializers import PatientSerializer
from .models import Patient

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ListPatientsView(APIView):
    '''
    Vista basada en clase para listar y crear pacientes.
    Métodos soportados:
    - GET: Devuelve una lista de todos los pacientes.
    - POST: Crea un nuevo paciente con los datos proporcionados en el cuerpo de la solicitud.
    Parámetros:
    - request: Objeto de solicitud HTTP.
    Retorna:
    - Response: Objeto de respuesta HTTP con los datos solicitados o el resultado de la creación.
    Notas: La creación de un nuevo paciente requiere que se envíen todos los campos obligatorios.
    '''
    allowed_methods = ['GET', 'POST']

    def get(self, request) -> Response:
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request) -> Response:
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Permite lanzar una excepción si no es válido
        patient = serializer.save()  # Guardar el paciente en la base de datos
        return Response(PatientSerializer(patient).data, status=status.HTTP_201_CREATED)  # Devolver los datos del paciente creado
        
class DetailPatientView(APIView):
    '''
    Vista basada en clase para recuperar, actualizar o eliminar un paciente específico por su ID.
    Métodos soportados:
    - GET: Devuelve los detalles del paciente.
    - PUT: Actualiza los detalles del paciente con los datos proporcionados en el cuerpo de la solicitud.
    - DELETE: Elimina el paciente.
    Parámetros:
    - request: Objeto de solicitud HTTP.
    - pk: ID del paciente a recuperar, actualizar o eliminar.
    Retorna:
    - Response: Objeto de respuesta HTTP con los datos solicitados, el resultado de la actualización o la confirmación de eliminación.
    Notas: La actualización requiere que se envíen todos los campos obligatorios.
    '''
    allowed_methods = ['GET', 'PUT', 'DELETE']

    def get_object(self, pk):
        '''
        Recupera un objeto Patient por su ID (pk).
        Parámetros:
        - pk: ID del paciente a recuperar.
        Retorna:
        - Patient: Objeto Patient si se encuentra, None si no existe.
        '''
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            return None

    def get(self, request, pk) -> Response:
        patient = self.get_object(pk) # Usar el método get_object para obtener el paciente
        if patient is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk) -> Response:
        patient = self.get_object(pk) # Usar el método get_object para obtener el paciente
        if patient is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        patient = serializer.save()
        return Response(PatientSerializer(patient).data, status=status.HTTP_200_OK)

    def delete(self, request, pk) -> Response:
        patient = self.get_object(pk) # Usar el método get_object para obtener el paciente
        if patient is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# GET /api/list_patients/ => listar pacientes
# POST /api/list_patients/ => crear paciente
@api_view(['GET', 'POST'])
def list_patients(request)-> Response:
    '''
    Lista todos los pacientes o crea un nuevo paciente.
    Métodos soportados:
    - GET: Devuelve una lista de todos los pacientes.
    - POST: Crea un nuevo paciente con los datos proporcionados en el cuerpo de la solicitud.
    Parámetros:
    - request: Objeto de solicitud HTTP.
    Retorna:
    - Response: Objeto de respuesta HTTP con los datos solicitados o el resultado de la creación.
    Notas: La creación de un nuevo paciente requiere que se envíen todos los campos obligatorios.
    '''
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): #Permite lanzar una excepción si no es válido
            patient = serializer.save()  # Guardar el paciente en la base de datos
            return Response(PatientSerializer(patient).data, status.HTTP_201_CREATED)  # Devolver los datos del paciente creado
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)  # Devolver errores de validación
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

# GET /api/detail_patient/<int:pk>/ => detalle paciente
# PUT /api/detail_patient/<int:pk>/ => actualizar paciente
# DELETE /api/detail_patient/<int:pk>/ => eliminar paciente
@api_view(['GET', 'PUT', 'DELETE'])
def detail_patient(request, pk) -> Response:
    '''
    Recupera, actualiza o elimina un paciente específico por su ID.
    Métodos soportados:
    - GET: Devuelve los detalles del paciente.
    - PUT: Actualiza los detalles del paciente con los datos proporcionados en el cuerpo de la solicitud.
    - DELETE: Elimina el paciente.
    Parámetros:
    - request: Objeto de solicitud HTTP.
    - pk: ID del paciente a recuperar, actualizar o eliminar.
    Retorna:
    - Response: Objeto de respuesta HTTP con los datos solicitados, el resultado de la actualización o la confirmación de eliminación.
    Notas: La actualización requiere que se envíen todos los campos obligatorios.
    '''
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid(raise_exception=True):
            patient = serializer.save()
            return Response(PatientSerializer(patient).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class ListPatientsWithListAPIView(ListAPIView, CreateAPIView, DestroyAPIView):
    '''
    Vista basada en clase para listar todos los pacientes.
    Atributos:
    - queryset: Conjunto de todos los objetos Patient.
    - serializer_class: Serializador a utilizar para Patient.
    - allowed_methods: Métodos HTTP permitidos (GET, POST, DELETE).
    Métodos:
    - ListAPIView: Proporciona la funcionalidad para listar objetos.
    - CreateAPIView: Proporciona la funcionalidad para crear nuevos objetos.
    - DestroyAPIView: Proporciona la funcionalidad para eliminar objetos.
    '''
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    allowed_methods = ['GET', 'POST', 'DELETE']