from django.db import models

# Create your models here.
class Doctor(models.Model):
    '''
    Modelo que representa a un doctor en el sistema.
    Contiene información personal y profesional relevante.
    * Atributos:
        - first_name: Nombre del doctor.
        - last_name: Apellido del doctor.
        - qualification: Título profesional del doctor.
        - contact_number: Número de contacto del doctor.
        - email: Dirección de correo electrónico del doctor.
        - address: Dirección del consultorio del doctor.
        - biography: Breve biografía del doctor.
        - specialty: Especialidad médica del doctor.
    * Métodos:
        - __str__: Retorna una representación legible del doctor.
    '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    qualification = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    biography = models.TextField(blank=True)
    specialty = models.CharField(max_length=100)
    is_on_vacation = models.BooleanField(default=False)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialty}"
    
class Departament(models.Model):
    '''
    Modelo que representa un departamento médico en el sistema.
    * Atributos:
        - name: Nombre del departamento.
        - description: Descripción del departamento.
    * Métodos:
        - __str__: Retorna una representación legible del departamento.
    '''
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class DoctorAvailability(models.Model):
    '''
    Modelo que representa la disponibilidad de un doctor.
    * Atributos:
        - doctor: Doctor al que pertenece la disponibilidad.
        - start_date: Fecha de inicio de la disponibilidad.
        - end_date: Fecha de fin de la disponibilidad.
        - start_time: Hora de inicio de la disponibilidad.
        - end_time: Hora de fin de la disponibilidad.
    * Métodos:
        - __str__: Retorna una representación legible de la disponibilidad.
    '''
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='availabilities')
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor.first_name} {self.doctor.last_name} - {self.start_date} ({self.start_time}-{self.end_time})"
    
class MedicalNote(models.Model):
    '''
    Modelo que representa una nota médica asociada a un doctor.
    * Atributos:
        - doctor: Doctor al que pertenece la nota médica.
        - note: Contenido de la nota médica.
        - created_at: Fecha y hora de creación de la nota médica.
    * Métodos:
        - __str__: Retorna una representación legible de la nota médica.
    '''
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='medical_notes')
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.note} - {self.doctor.first_name} {self.doctor.last_name}"