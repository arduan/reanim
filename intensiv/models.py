from django.db import models
from django.utils import timezone
from django.urls import reverse


class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=3)
    address = models.CharField(max_length=255, default="")
    phone = models.PositiveIntegerField()
    date_in = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        """
        Здесь мы используем функцию reverse() для генерации URL для представления
        patient_detail, которое должно принимать параметр pk.
        """
        return reverse('patient_detail',  kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return self.name


class VitalSigns(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    heart_rate = models.PositiveIntegerField()
    respiratory_rate = models.PositiveIntegerField()
    blood_pressure_systolic = models.PositiveIntegerField()
    blood_pressure_diastolic = models.PositiveIntegerField()
    oxygen_saturation = models.PositiveIntegerField()
    measurement_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patient.name
