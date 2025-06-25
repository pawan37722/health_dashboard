from django import forms
from .models import HealthEntry

class HealthEntryForm(forms.ModelForm):
    class Meta:
        model = HealthEntry
        fields = ['weight', 'sleep_hours', 'blood_pressure', 'sugar_level']
        widgets = {
            'weight': forms.NumberInput(attrs={'step': 0.1}),
            'sleep_hours': forms.NumberInput(attrs={'step': 0.1}),
            'sugar_level': forms.NumberInput(attrs={'step': 0.1}),
        }
