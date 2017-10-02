from django.db import models
from django.contrib import admin
from django.forms import CheckboxSelectMultiple

from .models import Delivery, Category, Location, Supplier


# Deliveries admin class for searching deliveries and filtering
# see delivery model for more information
class DeliveryAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Supplier info',   {'fields': ['supplier', 'location']}),
        ('Product',         {'fields': ['date', 'photo', 'categories', 'weight', 'note']}),
        ('Status',          {'fields': ['processing', 'active']}),
    ]

    formfield_overrides = {
        # Client wants to have checkboxes instead of a dropdown.
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    list_display = (
        'date', 'location', 'supplier', 'processing', 'category', 'active', 'image',
    )
    list_display_links = ('date',)
    ordering = ('-date',)
    list_per_page = 50


# Register your models here.
admin.site.site_header = 'Buurman - Materialmanager'
admin.site.register(Location)
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Delivery, DeliveryAdmin)
