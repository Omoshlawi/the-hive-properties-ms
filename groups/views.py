from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Group, GroupProperties
from .serializers import GroupSerializer ,GroupPropertiesSerializer, GroupWithPropertiesSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'slug'
    # lookup_url_kwarg = 'slug'


class GroupPropertiesViewSet(viewsets.ModelViewSet):
    queryset = GroupProperties.objects.all()
    serializer_class = GroupPropertiesSerializer
