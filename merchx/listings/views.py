from django.shortcuts import render, redirect
from django.http import Http404
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ListingForm
from django.core.mail import send_mail

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

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()

    return render(request, 'listings/band_create.html', {'form': form})

def band_update(request, band_id):
    band = Band.objects.get(id = band_id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band_id)
        
    else:
        form = BandForm(instance=band)

    return render (request, 'listings/band_update.html', {'form': form})

def about(request):
    return render(request, 'listings/about.html')


def contact(request):
    return render(request, 'listings/contact.html')

def listings(request):
    listings = Listing.objects.all()
    
    if request.method == 'POST':
        form = ListingForm(request.POST)
        
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)

    else:
        form = ListingForm()

    return render(request, 'listings/listings.html', {'listings': listings, 'form': form})

def listing_detail(request, listing_id):
    try:
        listing = Listing.objects.get(id = listing_id)
        band = Band.objects.get(id = listing.band_id)
    except Listing.DoesNotExist:
        raise Http404
    return render(request, 'listings/listing_detail.html', {'listing': listing, 'band': band})


def listing_update(request, listing_id):
    listing = Listing.objects.get(id = listing_id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing-detail', listing_id)
        
    else:
        form = ListingForm(instance=listing)
        
    return render (request, 'listings/listing_update.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"]} via MecherX',
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["mendos.prod@gmail.com"]
            )
        return redirect('band-list')
    
    else: 
        form = ContactUsForm()

    return render(request, 'listings/contact.html', {'form': form})

