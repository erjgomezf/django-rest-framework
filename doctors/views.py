from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .serializers import DoctorSerializer
from .models import Doctor

# Create your views here.
@api_view(['GET', 'POST'])
def list_doctors(request) -> Response:
    '''
    Lista todos los doctores o crea un nuevo doctor.
    Métodos soportados:
    - GET: Devuelve una lista de todos los doctores.
    - POST: Crea un nuevo doctor con los datos proporcionados en el cuerpo de la solicitud.
    Parámetros:
    - request: Objeto de solicitud HTTP.
    Retorna:
    - Response: Objeto de respuesta HTTP con los datos solicitados o el resultado de la creación.
    Notas: La creación de un nuevo doctor requiere que se envíen todos los campos obligatorios.
    '''
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): #Permite lanzar una excepción si no es válido
            doctor = serializer.save()  # Guardar el doctor en la base de datos
            return Response(DoctorSerializer(doctor).data, status=status.HTTP_201_CREATED)  # Devolver los datos del doctor creado
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Devolver errores de validación
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'PUT', 'DELETE'])
def detail_doctor(request, pk) -> Response:
    '''
    Recupera, actualiza o elimina un doctor específico por su ID.
    Métodos soportados:
    - GET: Devuelve los detalles del doctor.
    - PUT: Actualiza los detalles del doctor con los datos proporcionados en el cuerpo de la solicitud.
    - DELETE: Elimina el doctor.
    Parámetros:
    - request: Objeto de solicitud HTTP.
    - pk: ID del doctor a recuperar, actualizar o eliminar.
    Retorna:
    - Response: Objeto de respuesta HTTP con los datos solicitados o el resultado de la operación.
    Notas: La actualización de un doctor requiere que se envíen todos los campos obligatorios.
    '''
    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid(raise_exception=True):
            doctor = serializer.save()
            return Response(DoctorSerializer(doctor).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)