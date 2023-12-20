from django.utils.text import slugify
import os

PROPERTY_MEDIA = 'properties'


def property_images(instance, filename):
    return os.path.join(PROPERTY_MEDIA, slugify(instance.title), slugify(filename))


def property_unit_images(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (slugify(instance.unit.name), ext)
    return os.path.join(PROPERTY_MEDIA, slugify(instance.unit.name), filename)
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (slugify(instance.property.name), ext)
    return os.path.join(PROPERTY_MEDIA, slugify(instance.property.name), filename)