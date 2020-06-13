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
    # required_css_class = 'required'
    # color = forms.CharField(label='Окрас', max_length=100)
    # weight = forms.CharField(label='Вес')
    # photoUrl = forms.URLField(label='Ссылка на фото')
    user_id = forms.HiddenInput()
    # (attrs={'class': 'form-control'})
    description = forms.CharField(max_length=10000)
    # (attrs={'class': 'form-control'})
    geotag = forms.CharField(max_length=100)
    # (attrs={'class': 'form-control', 'id': 'geometka'})
    status = forms.CharField(max_length=20)
    # (attrs={'class': 'form-control'})
    photoURL = forms.CharField(max_length=500)
    # (attrs={'class': 'form-control'})