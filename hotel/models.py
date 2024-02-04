from django.db import models
from django.contrib.auth.models import User
from .constants import BOOKING_TYPES, BOOKING_STATUS
# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length = 20)
    description = models.TextField()
    image = models.ImageField(upload_to="service/images/")

    def __str__(self):
        return self.name
    
class BookingHotel(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    address = models.CharField(max_length = 100)
    booking_type = models.CharField(max_length = 10, choices = BOOKING_TYPES)
    booking_status = models.CharField(max_length = 10, choices = BOOKING_STATUS)

    def __str__(self):
        return self.name