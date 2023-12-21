from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

from core.models import PublishableBaseModel, ImageBaseModel
from listings.utils import listing_images


# Create your models here.





class Listing(PublishableBaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    available = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    date_listed = models.DateField(default=timezone.now)
    featured = models.BooleanField(default=False)
    tags = TaggableManager()
    amenities = models.TextField(null=True, blank=True, help_text="Comma separated amenities")

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    """
    Amenities: Features or amenities associated with the entire listing, applicable to all properties.
    """


class ListingImage(ImageBaseModel):
    image = models.ImageField(null=False, blank=False, upload_to=listing_images)
    listing = models.ForeignKey("listings.Listing", on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"{self.listing.title} image"

class ListingProperty(models.Model):
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

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = "Listing Properties"


class RentalListing(Listing):
    deposit_required = models.DecimalField(max_digits=10, decimal_places=2)
    renewal_interval = models.PositiveIntegerField()


class SaleListing(Listing):

    closing_date = models.DateField(null=True, blank=True)
    mortgage_options = models.TextField(null=True, blank=True)
