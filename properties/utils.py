from django.utils.text import slugify
import os

PROPERTY_MEDIA = 'properties'


def property_images(instance, filename):
    destination = slugify(instance.property.title)
    name, ext = filename.split('.')
    filename = "%s.%s" % (slugify(name), ext)
    return os.path.join(PROPERTY_MEDIA, destination, filename)
