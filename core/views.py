from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView



from .models import Car, Brand
from .serializers import CarSerializer, BrandSerializer
from .permissions import CustomPermissons, AllowStaff




class BrandListCreateAPIView(ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [CustomPermissons, AllowStaff]


class BrandDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [CustomPermissons, AllowStaff]




class CarListCreateAPIView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = [CustomPermissons, AllowStaff]



class CarDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = [CustomPermissons, AllowStaff]



