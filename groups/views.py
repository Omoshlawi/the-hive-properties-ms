from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Group, PropertyGroupMemberShip
from .serializers import GroupSerializer ,PropertyGroupMemberShipSerializer, GroupWithPropertiesSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'slug'
    # lookup_url_kwarg = 'slug'


class GroupPropertiesViewSet(viewsets.ModelViewSet):
    queryset = PropertyGroupMemberShip.objects.all()
    serializer_class = PropertyGroupMemberShipSerializer
