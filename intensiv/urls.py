from django.urls import path
from .views import VitalSignsListView, VitalSignsCreateView, PatientListView, VitalSignsDetailView

app_name = 'patients'

urlpatterns = [
    path('', PatientListView.as_view(), name='patient_list'),
    path('vital/', VitalSignsListView.as_view(), name='vital_signs_list'),
    path('<int:pk>/vital-signs/', VitalSignsDetailView.as_view(), name='vital_signs_detail'),
    path('add/', VitalSignsCreateView.as_view(), name='vital_signs_create'),
]
