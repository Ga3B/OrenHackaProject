from django import forms
from django.forms import ModelForm
from .models import Request
from django.db import models


# class QueryForm(forms.Form):
#     # required_css_class = 'required'
#     color = forms.CharField(label='Окрас', max_length=100)
#     weight = forms.CharField(label='Вес')
#     photoUrl = forms.URLField(label='Ссылка на фото')
#

class RequsetForm(forms.Form):
    class Meta:
        model = Request
        fields = ['dateTime', 'user_id', 'description', 'geotag', 'status', 'photoURL',]
        widgets = {
        'user_id': forms.HiddenInput(attrs={'class': 'form-control'}),
        'description': forms.TimeInput(attrs={'class': 'form-control'}),
        'geotag': forms.HiddenInput(attrs={'class': 'form-control', 'id': 'geometka'}),
        'status': forms.HiddenInput(attrs={'class': 'form-control'}),
        'photoURL': forms.TextInput(attrs={'class': 'form-control'}),
        }
