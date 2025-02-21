from django.contrib import admin
from listings.models import Band, Listing
# Register your models here.
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'year_formed', 'active')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'sold', 'year', 'type', 'band')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
