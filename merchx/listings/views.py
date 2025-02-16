from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing

# Create your views here.
def hello(request):
    bands = Band.objects.all()
    listings = Listing.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})

def about(request):
    return render(request, 'listings/about.html')


def contact(request):
    return render(request, 'listings/contact.html')


def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listings})
