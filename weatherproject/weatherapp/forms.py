from django import forms
from .models import City

class CityForm(forms.Form):
    city = forms.CharField(
        label='City Name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter city name...',
        })
    )