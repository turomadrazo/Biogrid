from django import forms
from .models import Biography

class BiographyForm(forms.ModelForm):
    class Meta: 
        model = Biography
        fields = ['name','occupation','birth','death','nationality','image','summary']
        