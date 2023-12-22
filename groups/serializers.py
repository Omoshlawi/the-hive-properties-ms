from rest_framework import serializers
from .models import Group, PropertyGroupMemberShip
from properties.models import Property  # Assuming you have a Property model in a 'properties' app
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class PropertyGroupMemberShipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PropertyGroupMemberShip
        fields = ['id', 'url', 'group', 'property', 'date_joined', 'notes', 'created_at', 'updated_at']
        extra_kwargs = {
            'url': {'view_name': "groups:group-properties-detail"},
            'group': {'view_name': "groups:group-detail", 'lookup_field': "slug"},
            'property': {'view_name': "properties:property-detail", 'lookup_field': "slug"},
        }


class NestedGroupSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Group
        fields = [
            'url', 'id', 'title', 'slug', 'description',
            'tags', 'cover_image', 'created_at',
            'updated_at', "properties"
        ]
        extra_kwargs = {
            'url': {'view_name': 'groups:group-detail', 'lookup_field': "slug"},
        }


class NestedPropertyGroupMemberShipSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PropertyGroupMemberShip
        fields = ['id', 'url', 'group', 'property', 'date_joined', 'notes', 'created_at', 'updated_at']
        extra_kwargs = {
            'url': {'view_name': "groups:group-properties-detail"},
            'group': {'view_name': "groups:group-detail", 'lookup_field': "slug"},
            'property': {'view_name': "properties:property-detail", 'lookup_field': "slug"},
        }


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagListSerializerField()
    memberships = PropertyGroupMemberShipSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = [
            'url', 'id', 'title', 'slug', 'description',
            'tags', 'cover_image', 'created_at',
            'updated_at', "memberships"
        ]
        extra_kwargs = {
            'url': {'view_name': 'groups:group-detail', 'lookup_field': "slug"},
        }


#


#
#
class GroupWithPropertiesSerializer(GroupSerializer):
    properties = PropertyGroupMemberShipSerializer(many=True, read_only=True)

    class Meta(GroupSerializer.Meta):
        fields = GroupSerializer.Meta.fields + ['properties']
