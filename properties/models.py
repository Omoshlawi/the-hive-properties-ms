from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from taggit.managers import TaggableManager

from core.models import PublishableBaseModel, ImageBaseModel
from properties.utils import property_unit_images, property_images


# Create your models here.


class PropertyImage(ImageBaseModel):
    image = models.ImageField(null=False, blank=False, upload_to=property_images)
    property = models.ForeignKey("properties.Property", on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"{self.property.title} image"


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
    sqft_size = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    date_build = models.DateField(null=True, blank=True)

    def primary_image(self):
        images = self.images.filter(is_primary=True)
        return images.first() if images.exists() else None

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)


@receiver(post_save, sender=Property)
def update_slug_on_save(sender, instance, **kwargs):
    """
    Signal receiver to update the slug after a Property instance is saved.
    """
    instance.slug = slugify(f"{instance.title}-{instance.id}")
    instance.save(update_fields=['slug'])


class Amenity(models.Model):
    property = models.ForeignKey("properties.Property", on_delete=models.CASCADE, related_name="amenities")
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('property', 'name')
