# hotel/models.py
from django.db import models
from django.contrib.auth.models import User
from hotel.constants import STAR_CHOICES

class Hotel(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="service/images/")

    def __str__(self):
        return self.name
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.CharField(choices=STAR_CHOICES, max_length=10)

    def __str__(self):
        return f"User: {self.user.username} - Hotel: {self.hotel.name}"
