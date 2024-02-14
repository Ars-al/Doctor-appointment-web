from .models import Appointment

def get_notifications(request):
    count = Appointment.objects.filter(accepted=False).count()
    context = {
        'count': count,
    }
    return context