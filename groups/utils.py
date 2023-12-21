import os

from django.utils.text import slugify

GROUPS_MEDIA = 'groups'


def group_images(instance, filename):
    destination = slugify(instance.title)
    name, ext = filename.split('.')
    filename = "%s.%s" % (slugify(name), ext)
    return os.path.join(GROUPS_MEDIA, destination, filename)