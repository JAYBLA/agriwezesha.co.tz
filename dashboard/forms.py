from django import forms
from .models import Job
from bootstrap_modal_forms.forms import BSModalModelForm


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['title', 'responsibilities', 'skills','qualifications',]

        