from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import VitalSigns, Patient
from django.views.generic import ListView


class PatientListView(ListView):
    model = Patient
    template_name = 'patient_list.html'
    context_object_name = 'patient_list'


class VitalSignsListView(ListView):
    """
    VitalSignsListView - отображение списка всех записей о витальных функциях. 
    model указывает на модель, template_name определяет имя шаблона для отображения, 
    а context_object_name определяет имя переменной, которая будет передаваться в шаблон.
    """
    model = VitalSigns
    template_name = 'vital_signs_list.html'
    context_object_name = 'vital_signs'


class PatientDetailView(DetailView):
    """
    Отображение деталей записи о витальных функциях пациента.
    model, template_name и context_object_name определены так же, как и в VitalSignsListView.
    """
    model = Patient
    template_name = 'vital_signs_detail.html'
    context_object_name = 'patient_detail'


class VitalSignsCreateView(CreateView):
    """
    VitalSignsCreateView - форма для создания новой записи о витальных функциях. 
    model указывает на модель, template_name определяет имя шаблона для отображения формы, 
    а fields определяет поля модели, которые будут отображаться в форме.
    """
    model = VitalSigns
    template_name = 'vital_signs_form.html'
    fields = '__all__'


class VitalSignsUpdateView(UpdateView):
    """
    VitalSignsUpdateView - форма для обновления существующей записи о витальных функциях. 
    Параметры класса такие же, как в VitalSignsCreateView.
    """
    model = VitalSigns
    template_name = 'vital_signs_form.html'
    fields = '__all__'


class VitalSignsDeleteView(DeleteView):
    """
    VitalSignsDeleteView - форма для удаления записи о витальных функциях. model указывает на модель, 
    template_name определяет имя шаблона для отображения формы подтверждения удаления, 
    а success_url указывает URL-адрес, на который пользователь будет перенаправлен 
    после удаления записи.
    """
    model = VitalSigns
    template_name = 'vital_signs_confirm_delete.html'
    success_url = reverse_lazy('vital_signs_list')
