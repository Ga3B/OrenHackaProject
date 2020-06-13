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

class RequestForm(forms.Form):
    description = forms.CharField(max_length=10000)
    geotag = forms.CharField(max_length=100)
    status = forms.CharField(max_length=20)
    photoURL = forms.URLField(max_length=500)
