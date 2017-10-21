from __future__ import unicode_literals

from django.conf import settings
from django_resized import ResizedImageField
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

if settings.DEBUG:
    link = 'http://127.0.0.1:8000'

else:
    link = 'http://buurman.nickderonde.tech'


# location model
class Location(models.Model):
    location = models.CharField(max_length=50, null=False, blank=False)
    pass

    class Meta:
        db_table = "location"
        verbose_name_plural = "locations"

    def __str__(self):
        return self.location


# supplier model
class Supplier(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    Headquarters_location = models.ForeignKey('Location', related_name='Supplier')

    class Meta:
        db_table = "supplier"

    def __str__(self):
        return self.name


# category model
class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    pass

    class Meta:
        db_table = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


# function for the upload_location
def upload_location(instance: object, filename: object) -> object:
    return "%s/%s" % (instance.date.strftime('%Y'), filename)


# Delivery model
class Delivery(models.Model):
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(default=timezone.now)
    photo = ResizedImageField(size=[1920, 1080],
                              quality=75,
                              upload_to=upload_location,
                              blank=False,
                              null=False)
    # height_field = models.IntegerField(default=0)
    # width_field = models.IntegerField(default=0)
    PROCESSING_CHOICES = (
        (0, '0%'),
        (25, '25%'),
        (50, '50%'),
        (75, '75%'),
        (100, '100%'),
    )
    processing = models.IntegerField(
        choices=PROCESSING_CHOICES,
        default=25,
    )
    categories = models.ManyToManyField(Category)
    weight = models.IntegerField(null=True, blank=True)
    note = models.TextField(null=True, blank=True, max_length=1000)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "delivery"
        verbose_name_plural = "deliveries"
        ordering = ('date', 'supplier', 'processing', 'weight',)

    def __str__(self):
        return self.date.strftime("%A, %d. %B %Y %I:%M%p")

    # Function for showing the image thumb in the list Delivery.admin
    def image(self):
        return '<a href="%s"' % self.photo.url + '><img src="%s" alt="Uploaded picture" width="150"/></a>' \
                                                 % self.photo.url

    # Function for showing the full image
    def image_full(self):
        return "%s" % self.photo.url

    # Function for showing the full image
    def image_pdf(self):
        return link + self.photo.url

    image.allow_tags = True

    # return the model categories as string manytomany
    def category(self):
        return_string = ""
        for category in self.categories.all():
            return_string += str(category)
            return_string += ", "
        return return_string

    def get_absolute_url(self):
        return reverse('delivery:detail', kwargs={'pk': self.pk})
