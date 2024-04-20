from django.contrib import admin
from .models import Production, RunRequest, Vendor, Location

# Register your models here.

admin.site.register(Production)
admin.site.register(RunRequest)
admin.site.register(Vendor)
admin.site.register(Location)