from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band

# Create your views here.
def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello, world!</h1>
        <p>Mes groupes préférés sont:</p>
        <ul>
            <li>Band 1: {bands[0].name}</li>
            <li>Band 2: {bands[1].name}</li>
            <li>Band 3: {bands[2].name}</li>
        </ul>
    """)

def about(request):
    return HttpResponse("<h1>About US</h1> <p>This is the about page</p>")

