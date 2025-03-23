from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpatialPointViewSet, SpatialPolygonViewSet

router = DefaultRouter()
router.register(r'points', SpatialPointViewSet)
router.register(r'polygons', SpatialPolygonViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
