from django.urls import path, include
from .views import VitalSignsListView, VitalSignsCreateView, PatientListView, PatientDetailView
from .resources import PatientResource, VitalSignsResource
app_name = 'patients'
patient_resource = PatientResource()
vital_signs = VitalSignsResource()

urlpatterns = [
    path('', PatientListView.as_view(), name='patient_list'),
    path('vital/', VitalSignsListView.as_view(), name='vital_signs_list'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('add/', VitalSignsCreateView.as_view(), name='vital_signs_create'),
    path('api/', include(patient_resource.urls)),
    path('api/', include(vital_signs.urls)),
]
