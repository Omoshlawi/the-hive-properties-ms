from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

from core.models import PublishableBaseModel
from groups.utils import group_images


# Create your models here.


class Group(PublishableBaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    tags = TaggableManager()
    cover_image = models.ImageField(upload_to=group_images, null=True, blank=True)
#     amenities


class GroupProperties(PublishableBaseModel):
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE, related_name='properties')
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE, related_name='groups')
    date_joined = models.DateTimeField(default=timezone.now)
    notes = models.TextField(null=True, blank=True)

    # class Meta:
    #     unique_together = ('group', 'property')
