from rest_framework import serializers
from .models import Appointment, MedicalNote
from doctors.models import Doctor

class AppointmentSerializer(serializers.ModelSerializer):
    '''
    Serializer del modelo Appointment.
    Incluye todos los campos del modelo.
    * Atributos:
        - model: Modelo asociado (Appointment).
        - fields: Campos a incluir en la serialización (todos los campos).
    * Métodos:
        - Meta: Clase interna que define la configuración del serializer.
    '''
    
    # Asegura que solo se puedan asignar doctores que no estén de vacaciones.
    doctor = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.filter(is_on_vacation=False)
    )
    class Meta:
        model = Appointment
        fields = '__all__'
        
        read_only_fields = ['id', 'patient']

class MedicalNoteSerializer(serializers.ModelSerializer):
    '''
    Serializer del modelo MedicalNote.
    Incluye todos los campos del modelo.
    * Atributos:
        - model: Modelo asociado (MedicalNote).
        - fields: Campos a incluir en la serialización (todos los campos).
    * Métodos:
        - Meta: Clase interna que define la configuración del serializer.
    '''
    class Meta:
        model = MedicalNote
        fields = '__all__'