from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from MainApp.utills import *
from .models import Animals
from .forms import QueryForm


def index(request):
    return render(request, 'MainApp/index.html', {'Test': "Placeholder"})


def detail(request, animal_id):
    animal = get_object_or_404(Animals, pk=animal_id)
    return render(request, 'MainApp/detail.html', {'animal': animal})


def add_request(request):
    submitted = False
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            color = form.cleaned_data['color']
            weight = form.cleaned_data['weight']
            photoUrl = form.cleaned_data['photoUrl']
            animal = Animals(color=color, weight=weight, PhotoUrl=photoUrl)
            # is_anon = request.POST.get('anon', False)
            # if is_anon:
            #     animal.save()
            # else:
            #     if request.user.is_authenticated:
            #         animal.save()
            animal.save()

            return HttpResponseRedirect('?submitted=True')
    else:
        form = QueryForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'MainApp/add_request.html', {'form': form, 'submitted': submitted})
