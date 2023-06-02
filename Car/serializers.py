from rest_framework import serializers
from .models import CarOwner, Car

from .models import CarInspection

class CarOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOwner
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'



class CarInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInspection
        fields = '__all__'