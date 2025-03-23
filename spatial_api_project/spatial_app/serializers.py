from rest_framework import serializers
from .models import SpatialPoint, SpatialPolygon

class SpatialPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpatialPoint
        fields = '__all__'

class SpatialPolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpatialPolygon
        fields = '__all__'
