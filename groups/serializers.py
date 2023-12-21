from rest_framework import serializers
from .models import Group, GroupProperties
from properties.models import Property  # Assuming you have a Property model in a 'properties' app
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class GroupPropertiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupProperties
        fields = ['id', 'url', 'group', 'property', 'date_joined', 'notes', 'created_at', 'updated_at']
        extra_kwargs = {
            'url': {'view_name': "groups:group-properties-detail"},
            'group': {'view_name': "groups:group-detail", 'lookup_field': "slug"},
            'property': {'view_name': "properties:property-detail", 'lookup_field': "slug"},
        }


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagListSerializerField()
    properties = GroupPropertiesSerializer(read_only=True, many=True)

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


#


#
#
class GroupWithPropertiesSerializer(GroupSerializer):
    properties = GroupPropertiesSerializer(many=True, read_only=True)

    class Meta(GroupSerializer.Meta):
        fields = GroupSerializer.Meta.fields + ['properties']
