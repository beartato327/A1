from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from clients.models import Client
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.
class Vehicle(models.Model):
    latest_update = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='vehicles')
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    vin_number = models.CharField(max_length=50)
    date_of_purchase = models.DateField()
    date_of_last_service = models.DateTimeField()
    author =  models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)

    def __str__(self):
        return self.make
    
    def get_absolute_url(self):
        return reverse('vehicle_list')