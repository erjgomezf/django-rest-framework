from django.db import models
from doctors.models import Doctor
from patients.models import Patient

# Create your models here.
class Appointment(models.Model):
    '''
    Modelo que representa una cita médica en el sistema.
    * Atributos:
        - patient: Relación con el modelo Patient.
        - doctor: Relación con el modelo Doctor.
        - appointment_date: Fecha de la cita.
        - appointment_time: Hora de la cita.
        - notes: Notas referentes a la cita.
        - status: Estado de la cita (programada, completada, cancelada).
    * Métodos:
        - __str__: Retorna una representación legible de la cita.
    '''
    STATUS_CHOICES = [
        ('programada', 'Programada'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='programada')

    def __str__(self):
        return f"Appointment of {self.patient} with Dr. {self.doctor} on {self.appointment_date} at {self.appointment_time} - Status: {self.status}"
    
class MedicalNote(models.Model):
    '''
    Modelo que representa una nota médica asociada a una cita.
    * Atributos:
        - appointment: Relación con el modelo Appointment.
        - note: Contenido de la nota médica.
        - created_at: Fecha y hora de creación de la nota médica.
    * Métodos:
        - __str__: Retorna una representación legible de la nota médica.
    '''
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='medical_notes')
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.appointment} - Created at {self.created_at}"
    
