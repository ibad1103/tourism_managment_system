from django.db import models

class Page(models.Model):
    COUNTRY_CHOICES = [
        ('gl', 'Gilgit'),
        ('hz', 'Hunza'),
        ('sk', 'Skardu'),
        ('st', 'Swat Valley'),
        ('ak', 'Azad Kashmir'),
    ]

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pages/')
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES)  # renamed from 'type'
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class TouristDestination(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="destinations")
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.page.name})"



class TravelGuideline(models.Model):
    page = models.OneToOneField(
        Page,
        on_delete=models.CASCADE,
        related_name="guideline"
    )
    safety_level = models.CharField(max_length=50, choices=[
        ("Safe", "Safe"),
        ("Exercise Caution", "Exercise Caution"),
        ("Not Safe", "Not Safe"),
    ])
    advice = models.TextField()

    def __str__(self):
        return f"Guideline for {self.page.name}"
