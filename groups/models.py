from django.db import models
from django.utils import timezone

from core.models import PublishableBaseModel


# Create your models here.


class Group(PublishableBaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)


class GroupProperties(PublishableBaseModel):
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE, related_name='properties')
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE, related_name='groups')
    date_joined = models.DateTimeField(default=timezone.now)
