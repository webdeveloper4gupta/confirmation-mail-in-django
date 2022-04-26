from django import forms
from .models import mahajan

class aman(forms.ModelForm):
    class Meta:
        model=mahajan
        fields="__all__"
