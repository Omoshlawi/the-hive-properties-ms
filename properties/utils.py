from django.utils.text import slugify
import os

PROPERTY_MEDIA = 'properties'


def property_images(instance, filename):
    return os.path.join(PROPERTY_MEDIA, slugify(instance.title), slugify(filename))

