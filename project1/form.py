from dataclasses import field
from django import forms
from .models import *

class UserInputForm(forms.ModelForm):
    class Meta:
        model=UserInput
        fields=('a','b')