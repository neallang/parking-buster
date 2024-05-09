from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = "__all__"
        exclude = ['status','user_profile', 'notes']



class AdminViewForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['status', 'notes']  # Now includes 'notes'