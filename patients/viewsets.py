from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .serializers import PatientSerializer, MedicalRecordSerializer
from .models import Patient

# Create your views here.


class PatientViewSet(viewsets.ModelViewSet):
    '''
    Vista basada en conjunto de vistas para el modelo Patient.
    Proporciona operaciones CRUD completas para el modelo Patient.
    * Atributos:
        - serializer_class: Serializador para el modelo Patient.
        - queryset: Conjunto de todos los objetos Patient.
    '''
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    
    #Actions personalizado para agregar un nuevo historial medico
    @action(["POST", "GET"], detail=True, url_path="add-medical-record")
    def add_medical_record(self, request, pk) -> Response:
        '''
        Agrega un nuevo historial médico a un paciente existente.
        Parámetros:
        - request: Objeto de solicitud HTTP que contiene los datos del historial médico.
        - pk: ID del paciente al que se le agregará el historial médico.
        Retorna:
        - Response: Objeto de respuesta HTTP con el historial médico creado o errores de validación.
        '''
        patient = self.get_object()
        serializer = MedicalRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(patient=patient)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Action personalizado para mostrar el historial medico del paciente en formato JSON
    @action(["GET"], detail=True, url_path="medical-record")
    def medical_record(self, request, pk) -> Response:
        '''
        Recupera el historial médico de un paciente específico.
        Parámetros:
        - request: Objeto de solicitud HTTP.
        - pk: ID del paciente cuyo historial médico se va a recuperar.
        Retorna:
        - Response: Objeto de respuesta HTTP con los datos del historial médico del paciente.
        '''
        patient = self.get_object()
        medical_records = patient.medical_records.all()
        serializer = MedicalRecordSerializer(medical_records, many=True)
        return Response(serializer.data)