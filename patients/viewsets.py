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

    def get_serializer_class(self):
        '''
        Retorna el serializador apropiado según la acción.
        - Para `add_medical_record`, usa `MedicalRecordSerializer`.
        - Para el resto, usa el `PatientSerializer` por defecto.
        '''
        if self.action == 'add_medical_record':
            return MedicalRecordSerializer
        return super().get_serializer_class()

    #Actions personalizado para agregar un nuevo historial medico
    @action(detail=True, methods=["post"], url_path="add-medical-record")
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
        # Obtenemos el serializador a través del método que ya hemos definido
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(patient=patient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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