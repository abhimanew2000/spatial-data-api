from django.urls import path, include

urlpatterns = [
    path('', include('spatial_app.urls')),
]
