from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Car, Brand
from .serializers import CarSerializer, BrandSerializer
from .permissions import CustomPermissons, AllowStaff




class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [CustomPermissons]
    search_fields = ['name', 'summary']


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [CustomPermissons]
    filter_backends = [SearchFilter]
    search_fields = ['name', 'car_model', 'description', 'color']
    filterset_fields = ["brand__name", "price", "year"]


















# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView





# class BrandListCreateAPIView(ListCreateAPIView):
#     serializer_class = BrandSerializer
#     queryset = Brand.objects.all()
#     permission_classes = [CustomPermissons, AllowStaff]


# class BrandDetailAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = BrandSerializer
#     queryset = Brand.objects.all()
#     permission_classes = [CustomPermissons, AllowStaff]




# class CarListCreateAPIView(ListCreateAPIView):
#     serializer_class = CarSerializer
#     queryset = Car.objects.all()
#     permission_classes = [CustomPermissons, AllowStaff]



# class CarDetailAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = CarSerializer
#     queryset = Car.objects.all()
#     permission_classes = [CustomPermissons, AllowStaff]



