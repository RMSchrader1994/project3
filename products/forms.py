from django import forms
from .models import DLC

class DLCForm(forms.ModelForm):
    class Meta:
        model = DLC
        fields = ('name', 'description', 'price', 'image')