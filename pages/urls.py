from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_pages, name='all_pages'),
    path('<int:page_id>/', views.page_detail, name='page_detail'),
    path('<int:page_id>/destinations/', views.page_destinations, name='page_destinations'),
    path('<int:page_id>/travel-advice/', views.travel_advice, name='travel_advice'),
]
