from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Vehicle, Client
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'

    """ def get_queryset(self):
        return Vehicle.objects.filter(client=) """

class VehicleUpdateView(LoginRequiredMixin,UpdateView):
    model = Vehicle
    fields = ('client', 'make', 'model', 'vin_number', 'date_of_purchase','date_of_last_service', 'author')
    template_name = 'vehicle_edit.html'

class VehicleDetailView(LoginRequiredMixin,DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'
    login_url = 'login'

class VehicleDeleteView(LoginRequiredMixin,DeleteView):
    model = Vehicle
    template_name = 'vehicle_delete.html'
    success_url = reverse_lazy('vehicle_list')

class VehicleCreateView(LoginRequiredMixin,CreateView):
    model = Vehicle
    template_name = 'vehicle_new.html'
    fields = ('client','make','model','vin_number','date_of_purchase','date_of_last_service','author')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)