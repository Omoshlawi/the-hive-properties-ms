import os

from django.utils.text import slugify

LISTINGS_MEDIA = 'listings'


def listing_images(instance, filename):
    destination = slugify(instance.title)
    name, ext = filename.split('.')
    filename = "%s.%s" % (slugify(name), ext)
    return os.path.join(LISTINGS_MEDIA, destination, filename)
