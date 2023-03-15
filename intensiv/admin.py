from django.contrib import admin
from .models import Patient, VitalSigns

admin.site.register(Patient)

class VitalSignsAdmin(admin.ModelAdmin):
    list_display = ('patient', 'measurement_date', 'temperature', 'heart_rate', 'respiratory_rate', 'blood_pressure_systolic', 'blood_pressure_diastolic', 'oxygen_saturation')

admin.site.register(VitalSigns, VitalSignsAdmin)
