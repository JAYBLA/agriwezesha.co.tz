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
        
class DonateForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields= '__all__'

class PartinerForm(forms.ModelForm):
    class Meta:
        model = Partiner
        fields= ['name', 'organization', 'address', 'city','country', 'message']
        
