from django.shortcuts import render
from django.http import Http404
from listings.models import Band, Listing

# Create your views here.
def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, band_id):
    try:
        band = Band.objects.get(id = band_id)
    except Band.DoesNotExist:
        raise Http404
    return render(request, 'listings/band_detail.html', {'band': band})

def about(request):
    return render(request, 'listings/about.html')


def contact(request):
    return render(request, 'listings/contact.html')

def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listings})

def listing_detail(request, listing_id):
    try:
        listing = Listing.objects.get(id = listing_id)
        band = Band.objects.get(id = listing.band_id)
    except Listing.DoesNotExist:
        raise Http404
    return render(request, 'listings/listing_detail.html', {'listing': listing, 'band': band})
