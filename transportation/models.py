from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Driver(models.Model):
    production_title = models.CharField(max_length=150, null=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    driver_email = models.EmailField(_('email address'), null=True)
    occupation_code = models.CharField(max_length=4, null=True)
    rate = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    last_4 = models.CharField(max_length=6, null=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name

class Vehicle(models.Model):
    production_title = models.CharField(max_length=150, null=True)
    vehicle_type = models.CharField(max_length=150, null=True)
    vendor_name = models.CharField(max_length=100, null=True)
    vendor_unit_number = models.CharField(max_length=10, null=True)
    internal_unit_number = models.CharField(max_length=20, null=True)
    purchase_order = models.CharField(max_length=10, null=True)
    vehicle_notes = models.TextField(max_length=2000, null=True)
    assigned_driver = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.vehicle_type + " " + self.vendor_unit_number
