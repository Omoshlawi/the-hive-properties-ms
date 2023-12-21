from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager

from core.models import PublishableBaseModel, ImageBaseModel
from listings.utils import listing_images


# Create your models here.


class Listing(PublishableBaseModel):
    """
    Object that make property or properties available for rent, sale, lease, e.t.c
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    available = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    date_listed = models.DateField(default=timezone.now)
    featured = models.BooleanField(default=False)
    tags = TaggableManager()
    amenities = models.TextField(null=True, blank=True, help_text="Comma separated amenities")
    cover_image = models.ImageField(null=False, blank=False, upload_to=listing_images)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.title} image"


@receiver(post_save, sender=Listing)
def update_slug_on_save(sender, instance, **kwargs):
    """
    Signal receiver to update the slug after a Property instance is saved.
    """
    # Disconnect the post_save signal temporarily
    post_save.disconnect(update_slug_on_save, sender=Listing)

    # Update the slug
    instance.slug = slugify(f"{instance.title}-{instance.id}")
    instance.save(update_fields=['slug'])

    # Reconnect the post_save signal
    post_save.connect(update_slug_on_save, sender=Listing)


class ListingProperty(models.Model):
    """
    Objects that are listed as a unit/1 e.g Entire plot listed for sale as a whole will have units as listing property
    """
    listing = models.ForeignKey(
        'listings.Listing',
        on_delete=models.CASCADE,
        related_name='properties'
    )
    property = models.ForeignKey(
        'properties.Property',
        on_delete=models.CASCADE,
        related_name='listings'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.listing.title}-{self.property.title}"

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = "Listing Properties"
        unique_together = ('listing', 'property')


class RentalListing(models.Model):
    """
    Extends listing by adding specific information to rentals
    Is a one to many allowing one property to be listed for several purposes e.g. as commercial, residential rentals,e.t.c
    """
    listing = models.ForeignKey("listings.Listing", on_delete=models.CASCADE, related_name='rentals')
    deposit_required = models.DecimalField(max_digits=10, decimal_places=2)
    renewal_interval = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.listing.title} Rentals"


class SaleListing(models.Model):
    """
    Extends listing by adding specific information to sales

    """
    listing = models.ForeignKey("listings.Listing", on_delete=models.CASCADE, related_name='sales')
    down_payment_required = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="percentage of the property's total purchase price and demonstrates the buyer's commitment to the "
                  "purchase and serves as an initial contribution toward the property"
    )
    closing_date = models.DateField(null=True, blank=True)
    mortgage_options = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.listing.title} Sales"
