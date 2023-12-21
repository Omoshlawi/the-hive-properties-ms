import os

from django.utils.text import slugify

GROUPS_MEDIA = 'listings'


def group_images(instance, filename):
    return os.path.join(GROUPS_MEDIA, slugify(instance.title), slugify(filename))