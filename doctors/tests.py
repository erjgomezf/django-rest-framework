from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from patients.models import Patient
from .models import Doctor

# Create your tests here.
class DoctorViewSetTestCase(TestCase):
    def setUp(self):
        # Configuración inicial para las pruebas
        self.patient = Patient.objects.create(
            first_name="John Doe",
            last_name="Smith",
            date_of_birth="1990-01-01",
            contact_number="1234567890",
            email="john.doe@example.com",
            address="123 Main St",
            medical_history="No known allergies"
        )
        self.doctor = Doctor.objects.create(
            first_name="Dr. Jane",
            last_name="Doe",
            qualification="MD",
            graduation_date="2010-05-15",
            contact_number="0987654321",
            email="jane.doe@example.com",
            address="456 Elm St",
            biography="Experienced cardiologist",
            specialty="Cardiology",
            is_on_vacation=False
        )
        self.client = APIClient()

    # Prueba para verificar que la lista de citas de un doctor retorna 403 si no está autenticado
    def test_list_should_return_403(self):
        url = reverse(
            'doctors-get-appointments',
            kwargs={'pk': self.doctor.pk},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        
    '''
    def test_doctor_creation(self):
        # Prueba para la creación de un doctor
        response = self.client.post('/doctors/', {
            'first_name': 'Dr. Emily',
            'last_name': 'Johnson',
            'qualification': 'MD',
            'speciality': 'Pediatrics',
            'email': 'emily.johnson@example.com',
            'contact_number': '1231231234',
            'address': '789 Oak St',
            'biography': 'Pediatrician with 10 years of experience',
            'graduation_date': '2012-05-15',
            'is_on_vacation': False
        })
        self.assertEqual(response.status_code, 201)
    '''
    
    
    def test_doctor_list(self):
        # Prueba para listar doctores
        pass

    def test_doctor_detail(self):
        # Prueba para obtener detalles de un doctor
        pass

    def test_doctor_update(self):
        # Prueba para actualizar un doctor
        pass

    def test_doctor_delete(self):
        # Prueba para eliminar un doctor
        pass
