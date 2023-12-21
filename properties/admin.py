from django.contrib import admin

from properties.models import Property, PropertyImage, PropertyAttribute, Location


# Register your models here.


class PropertyImagesInline(admin.TabularInline):
    model = PropertyImage


class PropertyAttributeInline(admin.TabularInline):
    model = PropertyAttribute


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", 'slug', 'sqft_size', 'date_build', 'amenities', 'location')
    inlines = [PropertyAttributeInline, PropertyImagesInline]
    prepopulated_fields = {'slug': ('title',)}


class PropertiesInline(admin.TabularInline):
    model = Property


@admin.register(Location)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ('address', 'city', 'state', 'country', 'zip_code', 'longitude', 'latitude')
    inlines = [PropertiesInline]
