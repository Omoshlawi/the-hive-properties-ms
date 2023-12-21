import os

from django.utils.text import slugify

LISTINGS_MEDIA = 'listings'


def listing_images(instance, filename):
    return os.path.join(LISTINGS_MEDIA, slugify(instance.title), slugify(filename))