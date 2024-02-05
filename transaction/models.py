from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    hotel = models.ForeignKey('hotel.Hotel', related_name='bookings', on_delete=models.CASCADE)
    # check_in_date = models.DateField()
    # check_out_date = models.DateField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    is_confirmed = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])
    amount_deposited = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Subtract the amount deposited from the user's account balance
        self.user.account.balance -= self.amount_deposited
        self.user.account.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.hotel.name} - {self.check_in_date}"

    # class Meta:
    #     ordering = ['check_in_date']
