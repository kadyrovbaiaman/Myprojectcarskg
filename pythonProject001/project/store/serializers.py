from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarMake
        fields='__all__'



class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarModel
        fields='__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields=['id','car_name','category','description','price','with_photo','add_date']