from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime


# def index(request):
#     return render(request, 'index.html', {'Test': "Placeholder"})


def help(request):
    return render(request, 'help.html', {})


def contacts(request):
    return render(request, 'contacts.html', {})


def donate(request):
    return render(request, 'donate.html', {})
