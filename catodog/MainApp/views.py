from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from MainApp.utills import *
from .models import Request,Animals
from .forms import RequestForm
import datetime


def index(request):
    return render(request, 'MainApp/index.html')


def detail(request, animal_id):
    animal = get_object_or_404(Animals, pk=animal_id)
    return render(request, 'MainApp/detail.html', {'animal': animal})


def add_request(request):
    submitted = False
    if request.method == 'POST':

        form = RequestForm(request.POST)
        if form.is_valid():

            dateTime = datetime.datetime.now()
            user_id = request.user
            description = form.cleaned_data['description']
            geotag = form.cleaned_data['geotag']
            status = form.cleaned_data['status']
            photoUrl=form.cleaned_data['photoURL']
            req = Request(dateTime=dateTime, user_id=user_id, description=description,
                          geotag=geotag, status=status, photoURL=photoUrl)
            # is_anon = request.POST.get('anon', False)
            # if is_anon:
            #     animal.save()
            # else:
            #     if request.user.is_authenticated:
            #         animal.save()
            req.save()

            return HttpResponseRedirect('?submitted=True')
    else:

        form = RequestForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'MainApp/add_request.html', {'form': form, 'submitted': submitted})


def check_list(request):
    animals = Animals.objects.order_by('weight')[:5]
    return render(request, 'MainApp/check_list.html', {'animals': animals})


def about(request):
    return render(request, 'MainApp/about.html', {})


def pets(request):
    return render(request, 'MainApp/pets.html', {})


def news(request):
    return render(request, 'MainApp/news.html', {})
