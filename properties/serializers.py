from rest_framework import serializers
from taggit.serializers import TagListSerializerField

from .models import Property, Location, PropertyImage, PropertyAttribute


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ('id', "image",)


class PropertyAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAttribute
        fields = ('id', 'name', 'value')


class PropertiesSerializer(serializers.HyperlinkedModelSerializer):
    type = TagListSerializerField()
    property_location = serializers.SerializerMethodField()
    images = PropertyImageSerializer(many=True, read_only=True)
    attributes = PropertyAttributeSerializer(many=True, read_only=True)
    property_amenities = serializers.SerializerMethodField()

    def get_property_amenities(self, instance):
        return [] if not instance.amenities else list(
            map(
                lambda amenity: amenity.strip(), instance.amenities.split(',')
            )
        )

    def get_property_location(self, instance):
        return NestedLocationSerializer(instance=instance.location, context=self.context).data

    class Meta:
        model = Property
        fields = [
            'id', 'url', "title", 'slug', 'sqft_size', 'date_build',
            'type', 'description', 'property_location', 'images', 'attributes',
            'property_amenities', 'amenities', 'location', 'created_at', 'updated_at',
        ]
        extra_kwargs = {
            'url': {'view_name': "properties:property-detail", 'lookup_field': "slug"},
            'location': {'view_name': "properties:location-detail", "write_only": True},
            'amenities': {'write_only': True}
        }


class NestedLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = [
            'id', 'url', "address", 'city', 'state', 'country',
            'zip_code', 'longitude',
            'latitude', 'created_at', 'updated_at',
        ]
        extra_kwargs = {
            'url': {'view_name': "properties:location-detail", },
        }


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    properties = PropertiesSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = [
            'id', 'url', "address", 'city', 'state', 'country',
            'zip_code', 'longitude', 'properties',
            'latitude', 'created_at', 'updated_at',
        ]
        extra_kwargs = {
            'url': {'view_name': "properties:location-detail", },
        }
