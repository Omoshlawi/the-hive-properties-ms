from django.contrib import admin

from properties.models import Property, PropertyImage, PropertyAttribute


# Register your models here.


class PropertyImagesInline(admin.TabularInline):
    model = PropertyImage


class PropertyAttributeInline(admin.TabularInline):
    model = PropertyAttribute


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", 'slug', 'sqft_size', 'date_build', 'amenities', 'location')
    inlines = [PropertyAttributeInline, PropertyImagesInline]
