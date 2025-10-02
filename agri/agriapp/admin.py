from django.contrib import admin
from .models import Farmer, Crop, Advisory

admin.site.register(Farmer)
admin.site.register(Crop)
admin.site.register(Advisory)
