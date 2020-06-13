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
    geotag = forms.CharField(max_length=100)
    status = forms.HiddenInput()
    photoURL = forms.FileField(label='Фото')


class AnimalForm(forms.Form):
    color = forms.CharField(label='Окрас', max_length=100)
    weight = forms.CharField(label='Вес')
    photoUrl = forms.FileField(label='Фото')
    special_signs = forms.CharField(label="Особые приметы",max_length=100)
    view_animal = forms.CharField(label='Вид животного', max_length=140)
    gender = forms.CharField(label="Пол животного", max_length=100)
    behavior = forms.CharField(label="Поведение",max_length=50)



