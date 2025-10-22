from django.db import models
from pages.models import Page  # import from your Pages app

class TripDeal(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="trip_deals",)
    title = models.CharField(max_length=200)  # e.g. "5 Days Gilgit Tour"
    duration_days = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.page.name})"

class Booking(models.Model):
    trip = models.ForeignKey(TripDeal, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    travelers = models.PositiveIntegerField(default=1)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.trip.title} by {self.name}"
