from django.db import models

# Create your models here.
from django.contrib.gis.db import models

class SpatialPoint(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()

class SpatialPolygon(models.Model):
    name = models.CharField(max_length=100)
    area = models.PolygonField()
