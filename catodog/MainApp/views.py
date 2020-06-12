from django.shortcuts import render
from django.views.generic import View
from MainApp.utills import *
from .forms import *


def index(request):
    return render(request, 'index.html', {'Test': "Placeholder"})
