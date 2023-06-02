from django.shortcuts import render
from .models import CarInspection
from datetime import datetime


def inspection_center_dashboard(request):
    # Lấy thông tin về số lượng, danh sách xe đã được đăng kiểm hàng tháng
    monthly_count = CarInspection.get_monthly_inspection_count(month, year)
    monthly_inspections = CarInspection.objects.filter(
        inspection_date__month=month,
        inspection_date__year=year
    )

    # Lấy thông tin về danh sách xe sắp hết hạn đăng kiểm hàng tháng
    expiring_inspections = CarInspection.get_expiring_inspections(month, year)

    # Lấy thông tin về số lượng xe đăng kiểm mới và đăng kiểm lại hàng tháng
    new_count, renewal_count = CarInspection.get_new_and_renewal_inspections(month, year)

    # Đối tượng để ghi nhận kết quả đăng kiểm và cấp giấy chứng nhận đăng kiểm
    inspection = CarInspection()

    if request.method == 'POST':
        # Ghi nhận kết quả đăng kiểm và cấp giấy chứng nhận đăng kiểm
        inspection.record_inspection_result(
            inspection_number=request.POST['inspection_number'],
            inspection_date=request.POST['inspection_date'],
            expiration_date=request.POST['expiration_date']
        )

    context = {
        'monthly_count': monthly_count,
        'monthly_inspections': monthly_inspections,
        'expiring_inspections': expiring_inspections,
        'new_count': new_count,
        'renewal_count': renewal_count,
        'inspection': inspection,
    }

    return render(request, 'inspection_center_dashboard.html', context)


from rest_framework import generics
from .models import CarOwner, Car
from .serializers import CarOwnerSerializer, CarSerializer

class CarOwnerListCreateView(generics.ListCreateAPIView):
    queryset = CarOwner.objects.all()
    serializer_class = CarOwnerSerializer

class CarOwnerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarOwner.objects.all()
    serializer_class = CarOwnerSerializer

class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

from rest_framework import generics
from .models import CarInspection
from .serializers import CarInspectionSerializer

class CarInspectionListCreateView(generics.ListCreateAPIView):
    queryset = CarInspection.objects.all()
    serializer_class = CarInspectionSerializer

class CarInspectionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarInspection.objects.all()
    serializer_class = CarInspectionSerializer