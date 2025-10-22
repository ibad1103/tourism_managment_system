from django.shortcuts import render, redirect, get_object_or_404
from .models import TripDeal
from .forms import BookingForm

def home(request):
    deals = TripDeal.objects.all()
    return render(request, "trips/home.html", {"deals": deals})

def book_trip(request, deal_id):
    deal = get_object_or_404(TripDeal, id=deal_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.trip = deal
            booking.save()
            return redirect("booking_success")
    else:
        form = BookingForm()
    return render(request, "trips/book_trip.html", {"form": form, "deal": deal})

def booking_success(request):
    return render(request, "trips/booking_success.html")

