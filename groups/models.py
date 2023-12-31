from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
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
    def __str__(self):
        return self.title


@receiver(post_save, sender=Group)
def update_slug_on_save(sender, instance, **kwargs):
    """
    Signal receiver to update the slug after a Property instance is saved.
    """
    # Disconnect the post_save signal temporarily
    post_save.disconnect(update_slug_on_save, sender=Group)

    # Update the slug
    instance.slug = slugify(f"{instance.title}-{instance.id}")
    instance.save(update_fields=['slug'])

    # Reconnect the post_save signal
    post_save.connect(update_slug_on_save, sender=Group)


class PropertyGroupMemberShip(PublishableBaseModel):
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE, related_name='memberships')
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE, related_name='memberships')
    date_joined = models.DateTimeField(default=timezone.now)
    notes = models.TextField(null=True, blank=True)

    # class Meta:
    #     unique_together = ('group', 'property')
