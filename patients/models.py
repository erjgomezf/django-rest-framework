from django.db import models

# Create your models here.
class Patient(models.Model):
    '''
    Modelo que representa a un paciente en el sistema.
    Contiene información personal y médica relevante.
    Atributos:
    - first_name: Nombre del paciente.
    - last_name: Apellido del paciente.
    - date_of_birth: Fecha de nacimiento del paciente.
    - contact_number: Número de contacto del paciente.
    - email: Correo electrónico del paciente.
    - address: Dirección del paciente.
    - medical_history: Historial médico del paciente.
    Métodos:
    - __str__: Retorna una representación legible del paciente.
    '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Insurance(models.Model):
    '''
    Modelo que representa la información de seguro médico de un paciente.
    Atributos:
    - patient: Relación con el modelo Patient.
    - provider: Nombre del proveedor de seguro.
    - policy_number: Número de póliza del seguro.
    - expiration_date: Fecha de expiración del seguro.
    Métodos:
    - __str__: Retorna una representación legible del seguro.
    '''
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='insurances')
    provider = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=50)
    expiration_date = models.DateField()

    def __str__(self):
        return f"{self.provider} - {self.policy_number}"
    
class MedicalRecord(models.Model):
    '''
    Modelo que representa un registro médico asociado a un paciente.
    Atributos:
    - patient: Relación con el modelo Patient.
    - date: Fecha del registro médico.
    - diagnosis: Diagnóstico médico.
    - treatment: Tratamiento recomendado.
    - follow_up_date: Fecha de seguimiento.
    Métodos:
    - __str__: Retorna una representación legible del registro médico.
    '''
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    date = models.DateField(auto_now_add=True)
    diagnosis = models.TextField()
    treatment = models.TextField()
    follow_up_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"Record for {self.patient} on {self.date}"