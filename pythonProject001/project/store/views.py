from rest_framework import viewsets,permissions
from .models import *
from .serializers import*
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import CarFilter


class CarViewSet(viewsets.ModelViewSet):
    queryset =Car.objects.all()
    serializer_class=CarSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = CarFilter
    search_fields=['car_name']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class=CategorySerializer


class CarMakeViewSet(viewsets.ModelViewSet):
    queryset = CarMake.objects.all()
    serializer_class=CarMakeSerializer


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class=CarModelSerializer

