from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"
    
    
class Flight(models.Model):
    # The following two lines no longer needed since we are using ForeignKey
    # origin = models.CharField(max_length=64)
    # destination = models.CharField(max_length=64)
    
    # Instead of using CharField, we use ForeignKey to link to the Airport model
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    # "CASCADE" means if an airport is deleted, all flights with that airport as origin or destination will be deleted
    # "related_name" is used to specify the name of the reverse relation from Airport to Flight
    
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
    
