from django.shortcuts import render, get_object_or_404
from .models import Page, TravelGuideline


def all_pages(request):
    pagess = Page.objects.all()
    return render(request, 'pages/all_pages.html', {'pages': pagess})


def page_detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, 'pages/page_detail.html', {
        'page': page,
    })


def page_destinations(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    destinations = page.destinations.all()
    return render(request, "pages/page_destinations.html", {
        "page": page,
        "destinations": destinations
    })


def travel_advice(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    guideline = getattr(page, "guideline", None)
    return render(request, "pages/page_travel_advice.html", {
        "page": page,
        "guideline": guideline,
    })
