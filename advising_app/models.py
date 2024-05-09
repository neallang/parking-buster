from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # testing additional field (will b changed obvi)
    site_admin = models.BooleanField(default=False, help_text="Designates whether a user is treated as a site admin.")  # Changed to BooleanField
    website = models.URLField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Report(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    subject = models.CharField(verbose_name="Report Subject (Required)", default="", max_length=100)
    status = models.CharField(default="New", max_length=50, choices = (("In Progress", "In Progress"), ("Resolved", "Resolved")))
    license_plate = models.CharField(verbose_name="License Plate", default="", max_length=20, blank=True, null=True)
    color = models.CharField(verbose_name="Color", default="", max_length=20, blank=True, null=True)
    make_model = models.CharField(verbose_name="Make/Model", default="", max_length=100, blank=True, null=True)
    location = models.CharField(verbose_name="Location", default="", max_length=100, blank=True, null=True)
    description = models.TextField(verbose_name="Description (Required)", default="")
    supportDocs = models.FileField(verbose_name="Upload files", blank=True, null=True)
    notes = models.TextField(verbose_name="Admin Notes", default="", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
