from django.contrib import admin
from .models import TripDeal, Booking

@admin.register(TripDeal)
class TripDealAdmin(admin.ModelAdmin):
    list_display = ("title", "page", "duration_days", "price")

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "trip", "travelers", "created_at")
