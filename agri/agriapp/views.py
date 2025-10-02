from django.shortcuts import render
from .models import Farmer, Crop, Advisory

def home(request):
    farmer = Farmer.objects.first()
    crop = Crop.objects.first()

    if farmer and crop:
        advisory = Advisory.objects.filter(farmer=farmer, crop=crop).first()
    else:
        advisory = None

    context = {
        "farmer": farmer,
        "crop": crop,
        "advisory": advisory,
    }
    return render(request, "agriapp/home.html", context)
