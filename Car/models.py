from django.db import models

class CarOwner(models.Model):
    owner_type_choices = [
        ('agency', 'Cơ quan'),
        ('individual', 'Cá nhân'),
    ]
    
    owner_type = models.CharField(
        max_length=10,
        choices=owner_type_choices,
        default='individual',
    )
    agency_name = models.CharField(max_length=100, blank=True, null=True)
    agency_address = models.CharField(max_length=200, blank=True, null=True)
    agency_contact = models.CharField(max_length=20, blank=True, null=True)
    representative_name = models.CharField(max_length=100, blank=True, null=True)
    
    individual_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    emergency_contact = models.CharField(max_length=20, blank=True, null=True)
    license_number = models.CharField(max_length=20, blank=True, null=True)
    owner_code = models.CharField(max_length=20, blank=True, primary_key=True)
    traffic_violations = models.TextField(blank=True, null=True)
    
    def __str__(self):
        if self.owner_type == 'agency':
            return self.agency_name
        else:
            return self.individual_name

class Car(models.Model):
    registration_number = models.CharField(max_length=50, primary_key=True)
    registration_date = models.DateField(blank=True, null=True)
    license_plate = models.CharField(max_length=20, blank=True, null=True)
    registered_location = models.CharField(max_length=100, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    engine_capacity = models.FloatField(blank=True, null=True)
    power = models.FloatField(blank=True, null=True)
    torque = models.FloatField(blank=True, null=True)
    transmission = models.CharField(max_length=50, blank=True, null=True)
    seating_capacity = models.PositiveIntegerField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    fuel_consumption = models.FloatField(blank=True, null=True)
    suspension = models.CharField(max_length=100, blank=True, null=True)
    braking_system = models.CharField(max_length=100, blank=True, null=True)

    purpose_choices = [
        ('personal', 'Đi lại cá nhân'),
        ('passenger_service', 'Dịch vụ trở khách'),
        ('transportation_service', 'Dịch vụ vận tải'),
    ]
    purpose = models.CharField(
        max_length=100,
        choices=purpose_choices,
        default='personal',
    )
    
    owner = models.CharField(max_length=20, blank=True, null=True)
    owner = models.ForeignKey('CarOwner',to_field='owner_code', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.registration_number


class CarInspection(models.Model):
    inspection_number = models.CharField(max_length=20, primary_key=True)
    inspection_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    inspection_center = models.CharField(blank=True, null=True, max_length=100)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    owner = models.CharField(max_length=20, blank=True, null=True)
    owner = models.ForeignKey('CarOwner',to_field='owner_code', blank=True, null=True, on_delete=models.SET_NULL)
    @staticmethod
    def get_monthly_inspection_count(month, year):
        return VehicleInspection.objects.filter(
            inspection_date__month=month,
            inspection_date__year=year
        ).count()

    @staticmethod
    def get_expiring_inspections(month, year):
        return VehicleInspection.objects.filter(
            expiration_date__month=month,
            expiration_date__year=year
        )

    @staticmethod
    def get_new_and_renewal_inspections(month, year):
        inspections = VehicleInspection.objects.filter(
            inspection_date__month=month,
            inspection_date__year=year
        )

        new_count = inspections.count()
        renewal_count = VehicleInspection.objects.filter(
            inspection_date__lt=inspections[0].inspection_date
        ).count()

        return new_count, renewal_count

    def record_inspection_result(self, inspection_number, inspection_date, expiration_date):
        self.inspection_number = inspection_number
        self.inspection_date = inspection_date
        self.expiration_date = expiration_date
        self.save()