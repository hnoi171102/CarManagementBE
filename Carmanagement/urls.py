
from django.contrib import admin
from django.urls import path
from Car import views
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path,include

from rest_framework import routers

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Car.urls')),
]
