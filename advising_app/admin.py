# from django.contrib import admin

# # Register your models here.

# advising_app/admin.py
from django.contrib import admin
from .models import UserProfile, Report

admin.site.register(UserProfile)
admin.site.register(Report)

