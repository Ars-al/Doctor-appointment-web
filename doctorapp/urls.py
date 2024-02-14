from django.urls import path
from .views import HomeTemplate, AppointmentTemplate, ManageAppointmentTemplate

urlpatterns = [
    path('', HomeTemplate.as_view() , name='home'),
    path('make-appointment', AppointmentTemplate.as_view() , name='appointment'),
    path('manage-appointments', ManageAppointmentTemplate.as_view() , name='manage_appointments'),
]