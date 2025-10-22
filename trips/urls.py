from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="trips_home"),
    path("book/<int:deal_id>/", views.book_trip, name="book_trip"),
    path("success/", views.booking_success, name="booking_success"),
]
