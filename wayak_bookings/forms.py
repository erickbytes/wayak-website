from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
  class Meta:
    model = Booking
    fields = ['name', 'email', 'from_city', 'to_city', 'date', 'service']
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
      'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
      'from_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your departure city'}),
      'to_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your destination city'}),
      'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select a date'}),
      'service': forms.Select(attrs={'class': 'form-control'}, choices=[('bus', 'Bus'), ('hotel', 'Hotel')])
    }
