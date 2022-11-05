from django import forms
from .models import *
from bootstrap_modal_forms.forms import BSModalModelForm


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['title', 'responsibilities', 'skills','qualifications',]

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name',]

class ProjectPhotosForm(forms.ModelForm):

    class Meta:
        model = MultipleImage
        fields = ['images']

                