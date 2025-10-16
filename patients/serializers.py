from rest_framework import serializers
from .models import Patient, Insurance, MedicalRecord
from bookings.serializers import AppointmentSerializer
from datetime import date

# Create your serializers here.
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
    
    # Campo calculado para la edad del paciente.
    age = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = [
            'id',
            'first_name',
            'last_name',
            'age',
            'date_of_birth',
            'contact_number',
            'email',
            'address',
            'medical_history',
            'appointments'
        ]

    # Método para calcular la edad del paciente.
    def get_age(self, obj) -> int:
        '''
        Calcula la edad del paciente basado en su fecha de nacimiento.
        * Parámetros:
            - obj: Instancia del modelo Patient.
        * Retorna:
            - int: Edad del paciente en años.
        '''
        age_td = date.today() - obj.date_of_birth
        return int(age_td.days // 365.25)  # Aproximación considerando años bisiestos
    
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