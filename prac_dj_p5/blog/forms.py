from django import forms
from django.forms import ModelForm
from .models import Car, Driver

# Создаем форму Venue
class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ("concern", "model", "year_release", "vin_car", "buyer")
        widgets = {
            'concern': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'concern'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'model'}),
            'year_release': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'year_release'}),
            'vin_car': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'vin_car'}),
            'buyer': forms.Select(attrs={'class': 'form-select', 'placeholder': 'buyer'}),

        }