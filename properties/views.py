from django.shortcuts import render
from rest_framework import viewsets

from .models import Property, Location
# Create your views here.
from .serializers import PropertiesSerializer, NestedLocationSerializer, LocationSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertiesSerializer
    queryset = Property.objects.all()
    lookup_field = 'slug'


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
