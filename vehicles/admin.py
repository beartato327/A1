from django.contrib import admin
from .models import Vehicle
# Register your models here.
class VehicleAdmin(admin.ModelAdmin):
    list_display =['client','make','model','latest_update']

admin.site.register(Vehicle, VehicleAdmin)
