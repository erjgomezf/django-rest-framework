from rest_framework import serializers
from .models import Doctor, Departament, DoctorAvailability, MedicalNote

class DoctorSerializer(serializers.ModelSerializer):
    '''
    Serializer del modelo Doctor.
    Incluye todos los campos del modelo.
    * Atributos:
        - model: Modelo asociado (Doctor).
        - fields: Campos a incluir en la serialización (todos los campos).
    * Métodos:
        - Meta: Clase interna que define la configuración del serializer.
    '''
    class Meta:
        model = Doctor
        fields = '__all__'  

class DepartamentSerializer(serializers.ModelSerializer):
    '''
    Serializer del modelo Departament.
    Incluye todos los campos del modelo.
    * Atributos:
        - model: Modelo asociado (Departament).
        - fields: Campos a incluir en la serialización (todos los campos).
    * Métodos:
        - Meta: Clase interna que define la configuración del serializer.
    '''
    class Meta:
        model = Departament
        fields = '__all__'

class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    '''
    Serializer del modelo DoctorAvailability.
    Incluye todos los campos del modelo.
    * Atributos:
        - model: Modelo asociado (DoctorAvailability).
        - fields: Campos a incluir en la serialización (todos los campos).
    * Métodos:
        - Meta: Clase interna que define la configuración del serializer.
    '''
    class Meta:
        model = DoctorAvailability
        fields = '__all__'

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
