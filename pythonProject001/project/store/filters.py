from django_filters import FilterSet
from .models import Car

class CarFilter(FilterSet):
    class Meta:
        model=Car
        fields={
            'category':['exact'],
            'price':['gt','lt']
        }