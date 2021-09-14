from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields= ['name', 'phone', 'email', 'subject', 'message']


class ExpertForm(forms.ModelForm):
    class Meta:
        model = Expert
        fields= '__all__'
        
class MarketForm(forms.ModelForm):
    class Meta:
        model = Market
        fields= '__all__'
