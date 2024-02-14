from django.db import models

class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    request = models.TextField(blank=True)
    send_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        ordering = ["-send_date"]
    