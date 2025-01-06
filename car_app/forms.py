from django import forms
from .models import Car, InsurancePolicy

from django.db import connection

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'color']  # Include only relevant fields
        widgets = {
            'make': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car make'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car model'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'min': 1900, 'max': 2100}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car color'}),
        }

    # Example custom validation
    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year < 1900 or year > 2100:
            raise forms.ValidationError("Year must be between 1900 and 2100.")
        return year
