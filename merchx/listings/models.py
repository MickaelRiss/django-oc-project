from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Band(models.Model):
    def __str__(self):
        return f'{self.name}'
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.CharField(max_length=100)
    genre = models.CharField(choices = Genre.choices, max_length=4)
    biography = models.TextField()
    year_formed = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2025)])
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)


class Listing(models.Model):
    def __str__(self):
        return f'{self.title}'
    class Type(models.TextChoices):
        RECORDS = 'Records'
        CLOTHING = 'Clothing'
        POSTERS = 'Posters'
        MISCELLANEOUS = 'Miscellaneous'

    title = models.CharField(max_length=100)
    description = models.TextField()
    sold = models.BooleanField(default=False)
    year = models.IntegerField(null=True)
    type = models.CharField(choices=Type.choices, max_length=15)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)