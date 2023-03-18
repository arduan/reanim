from tastypie.resources import ModelResource
from .models import Patient


class PatientResource(ModelResource):
    class Meta:
        queryset = Patient.objects.all()
        resource_name = 'patient'

    
