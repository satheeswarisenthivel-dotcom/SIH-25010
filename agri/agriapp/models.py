from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    soil_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Crop(models.Model):
    name = models.CharField(max_length=100)
    season = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Advisory(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f"Advice for {self.farmer.name} - {self.crop.name}"
