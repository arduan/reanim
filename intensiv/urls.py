from django.urls import path
from .views import VitalSignsListView, VitalSignsCreateView, PatientListView, PatientDetailView

app_name = 'patients'

urlpatterns = [
    path('', PatientListView.as_view(), name='patient_list'),
    path('vital/', VitalSignsListView.as_view(), name='vital_signs_list'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('add/', VitalSignsCreateView.as_view(), name='vital_signs_create'),
]
