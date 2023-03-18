from tastypie.resources import ModelResource
from .models import Patient, VitalSigns


class PatientResource(ModelResource):
    class Meta:
        queryset = Patient.objects.all()
        resource_name = 'patient'


class VitalSignsResource(ModelResource):
    class Meta:
        queryset = VitalSigns.objects.all()
        resource_name = 'vital_signs'
