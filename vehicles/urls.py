from django.urls import path
from . import views
from .views import (
    VehicleListView,
    VehicleUpdateView,
    VehicleDetailView,
    VehicleDeleteView,
    VehicleCreateView,
)

urlpatterns = [
    path('',
        views.VehicleListView.as_view(), name='vehicle_list'),
    path('<int:pk>/vehicle_edit/',
        VehicleUpdateView.as_view(), name='vehicle_edit'),
    path('<int:pk>',
        VehicleDetailView.as_view(), name='vehicle_detail'),
    path('<int:pk>/delete/',
        VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('new/', VehicleCreateView.as_view(), name='vehicle_new'),
]