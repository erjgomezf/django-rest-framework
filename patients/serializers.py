from rest_framework import serializers
from .models import Patient, Insurance, MedicalRecord

class PatientSerializer(serializers.ModelSerializer):
    '''
    Serializer del modelo Patient.
    Incluye todos los campos del modelo.
    Atributos:
    - model: Modelo asociado (Patient).
    - fields: Campos a incluir en la serialización (todos los campos).
    Métodos:
    - Meta: Clase interna que define la configuración del serializer.
    '''
    class Meta:
        model = Patient
        fields = '__all__'

class InsuranceSerializer(serializers.ModelSerializer):
    '''
    Serializer del modelo Insurance.
    Incluye todos los campos del modelo.
    Atributos:
    - model: Modelo asociado (Insurance).
    - fields: Campos a incluir en la serialización (todos los campos).
    Métodos:
    - Meta: Clase interna que define la configuración del serializer.
    '''
    class Meta:
        model = Insurance
        fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    '''
    Serializer del modelo MedicalRecord.
    Incluye todos los campos del modelo.
    Atributos:
    - model: Modelo asociado (MedicalRecord).
    - fields: Campos a incluir en la serialización (todos los campos).
    Métodos:
    - Meta: Clase interna que define la configuración del serializer.
    '''
    class Meta:
        model = MedicalRecord
        fields = '__all__'