from django.contrib import admin

from listings.models import Listing, ListingProperty, RentalListing, SaleListing


# Register your models here.

class ListingPropertiesInline(admin.TabularInline):
    model = ListingProperty


class RentalListingsInline(admin.TabularInline):
    model = RentalListing


class SaleListingInline(admin.TabularInline):
    model = SaleListing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'available', 'price', 'date_listed', 'featured', 'amenities', 'cover_image')
    inlines = [ListingPropertiesInline, RentalListingsInline, RentalListingsInline]
