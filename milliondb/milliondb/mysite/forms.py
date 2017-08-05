from django import forms
from .models import Idol

class IdolForm(forms.Form):
    name = forms.CharField(label="名前")