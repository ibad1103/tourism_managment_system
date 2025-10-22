from django.contrib import admin
from .models import Page, TouristDestination, TravelGuideline


class TouristDestinationInline(admin.TabularInline):  # or admin.StackedInline
    model = TouristDestination
    extra = 2   # how many empty forms to show


class TravelGuidelineInline(admin.StackedInline):  # One-to-One looks better stacked
    model = TravelGuideline
    can_delete = False  # since one-to-one, usually only edit not delete
    extra = 0


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "description")
    inlines = [TouristDestinationInline, TravelGuidelineInline]  # <-- both inline


@admin.register(TouristDestination)
class TouristDestinationAdmin(admin.ModelAdmin):
    list_display = ("name", "page", "description")


@admin.register(TravelGuideline)
class TravelGuidelineAdmin(admin.ModelAdmin):
    list_display = ("page", "safety_level", "advice")
