
from django.contrib import admin
from django.urls import path
from Car import views
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path,include
from .views import CarOwnerListCreateView, CarOwnerRetrieveUpdateDestroyView, CarListCreateView, CarRetrieveUpdateDestroyView

from rest_framework import routers

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

from django.urls import path
from . import views

from .views import CarInspectionListCreateView, CarInspectionRetrieveUpdateDestroyView


urlpatterns = [
    path('inspection-center/', views.inspection_center_dashboard, name='inspection_center_dashboard'),
    path('car_owners/', CarOwnerListCreateView.as_view(), name='car-owner-list-create'),
    path('car_owners/<int:pk>/', CarOwnerRetrieveUpdateDestroyView.as_view(), name='car-owner-retrieve-update-destroy'),
    path('cars/', CarListCreateView.as_view(), name='car-list-create'),
    path('cars/<str:pk>/', CarRetrieveUpdateDestroyView.as_view(), name='car-retrieve-update-destroy'),
    path('car_inspections/', CarInspectionListCreateView.as_view(), name='car-inspection-list-create'),
    path('car_inspections/<inspection_number>/', CarInspectionRetrieveUpdateDestroyView.as_view(), name='car-inspection-retrieve-update-destroy'),
]