from django import forms
from django.forms import fields
from .models import Campagin

class CampaginForm(forms.ModelForm):
    class Meta:
        model = Campagin
        fields = [
            'title','location','number_of_funds','goal','description','image'
        ]
