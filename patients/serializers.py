from rest_framework import serializers
from .models import Patient, Insurance, MedicalRecord
from bookings.serializers import AppointmentSerializer


class PatientSerializer(serializers.ModelSerializer):
    '''
    Serializer del modelo Patient.
    Incluye todos los campos del modelo.
    * Atributos:
        - model: Modelo asociado (Patient).
        - fields: Campos a incluir en la serialización (todos los campos).
    * Métodos:
        - Meta: Clase interna que define la configuración del serializer.
    '''
    
    # Incluir detalles de las citas asociadas al historial médico.
    appointments = AppointmentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Patient
        fields = [
            'id',
            'first_name',
            'last_name',
            'date_of_birth',
            'contact_number',
            'email',
            'address',
            'medical_history',
            'appointments'
        ]

class InsuranceSerializer(serializers.ModelSerializer):
    '''
    Serializer del modelo Insurance.
    Incluye todos los campos del modelo.
    * Atributos:
        - model: Modelo asociado (Insurance).
        - fields: Campos a incluir en la serialización (todos los campos).
    * Métodos:
        - Meta: Clase interna que define la configuración del serializer.
    '''
    class Meta:
        model = Insurance
        fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    '''
    Serializer del modelo MedicalRecord.
    Incluye todos los campos del modelo.
    * Atributos:
        - model: Modelo asociado (MedicalRecord).
        - fields: Campos a incluir en la serialización (todos los campos).
    * Métodos:
        - Meta: Clase interna que define la configuración del serializer.
    '''
    
    class Meta:
        model = MedicalRecord
        # Definimos explícitamente los campos para tener más control.
        fields = [
            'id', 
            'patient', 
            'date', 
            'diagnosis', 
            'treatment', 
            'follow_up_date'
        ]
        # El paciente se asigna desde la URL, no debe ser editable en el formulario.
        # La fecha se añade automáticamente.
        read_only_fields = ['id', 'patient', 'date']