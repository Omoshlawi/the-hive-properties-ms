from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from taggit.managers import TaggableManager

from core.models import PublishableBaseModel, ImageBaseModel
from properties.utils import property_images


# Create your models here.


class Property(PublishableBaseModel):
    """
    Any object that generate income and expense
    For see by public if published
    """
    title = models.CharField(max_length=50, help_text="Property user friendly identity")
    type = TaggableManager(
        verbose_name='Type Tags',
        help_text="Property type tags since property can fall into multiple category"
    )
    slug = models.SlugField(unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    sqft_size = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True,
                                    help_text="Size in square foots")
    date_build = models.DateField(null=True, blank=True)
    amenities = models.TextField(null=True, blank=True, help_text="Comma separated amenities")
    location = models.ForeignKey("properties.Location", on_delete=models.CASCADE, related_name='properties')

    def primary_image(self):
        images = self.images.filter(is_primary=True)
        return images.first() if images.exists() else None

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = "Properties"


@receiver(post_save, sender=Property)
def update_slug_on_save(sender, instance, **kwargs):
    """
    Signal receiver to update the slug after a Property instance is saved.
    """
    # Disconnect the post_save signal temporarily
    post_save.disconnect(update_slug_on_save, sender=Property)

    # Update the slug
    instance.slug = slugify(f"{instance.title}-{instance.id}")
    instance.save(update_fields=['slug'])

    # Reconnect the post_save signal
    post_save.connect(update_slug_on_save, sender=Property)


class PropertyImage(ImageBaseModel):
    image = models.ImageField(null=False, blank=False, upload_to=property_images)
    property = models.ForeignKey("properties.Property", on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"{self.property.title} image"


class PropertyAttribute(models.Model):
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE, related_name='attributes')
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('property', 'name')
        ordering = ('-name',)


class Location(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state}, {self.country}, {self.zip_code}"

    class Meta:
        ordering = ('-created_at',)
