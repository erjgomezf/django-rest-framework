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
        - validate_email: Valida que el correo electrónico tenga un formato correcto.
        - validate: Valida que el número de contacto tenga al menos 10 dígitos si el doctor está de vacaciones.
    '''
    class Meta:
        model = Doctor
        fields = '__all__'  
        
    def validate_email(self, value)-> str:
        '''
        Valida que el correo electrónico tenga un formato correcto.
        * Parámetros:
            -   value: Valor del campo email a validar.
        * Retorna:
            -   str: Valor del campo email si es válido.
        * Lanza:
            -   serializers.ValidationError: Si el formato del correo electrónico es inválido.
        '''
        if "@gmail.com" not in value:
            raise serializers.ValidationError("El correo electrónico debe contener '@gmail.com'.")
        return value
    
    def validate(self, attrs)-> dict:
        '''
        Valida que el número de contacto tenga al menos 10 dígitos si el doctor está de vacaciones.
        * Parámetros:
            -   attrs: Diccionario de atributos del serializer.
        * Retorna:
            -   dict: Diccionario de atributos si la validación es exitosa.
        * Lanza:
            -   serializers.ValidationError: Si el número de contacto es inválido cuando el doctor está de vacaciones.
        '''
        if len(attrs['contact_number']) < 10 and attrs['is_on_vacation'] == True:
            raise serializers.ValidationError("Ingresa un numero valido antes de poner irte de vacaciones")
        return super().validate(attrs)

class DepartamentSerializer(serializers.ModelSerializer):
    '''
    Serializer del modelo Departament.
    Incluye todos los campos del modelo.
    * Atributos:ººººº
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
