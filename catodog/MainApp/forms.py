from django import forms
from django.forms import ModelForm
# from .models import Poll
from django.db import models


class QueryForm(forms.Form):
    # required_css_class = 'required'
    color = forms.CharField(label='Окрас', max_length=100)
    weight = forms.CharField(label='Вес')
    photoUrl = forms.URLField(label='Ссылка на фото')


class RequestForm(forms.Form):
    # required_css_class = 'required'
    user_id = forms.HiddenInput()
    description = forms.CharField(label='Описание', max_length=140)
    geotag = forms.HiddenInput()
    status = forms.HiddenInput()
    photoURL = forms.CharField(label='Фото')