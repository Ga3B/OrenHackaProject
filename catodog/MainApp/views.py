from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from MainApp.utills import *
from .models import Request, Animals, Visitor, Transfer
from .forms import RequestForm
from .models import Request, Animals, Visitor
from .forms import RequestForm, AnimalForm
import datetime


def index(request):
    return render(request, 'MainApp/index.html')


def detail(request, animal_id):
    animal = get_object_or_404(Animals, pk=animal_id)
    return render(request, 'MainApp/detail.html', {'animal': animal})


def add_request(request):
    submitted = False
    if request.method == 'POST':

        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():

            dateTime = datetime.datetime.now()
            user_id = request.user
            description = form.cleaned_data['description']
            geotag = form.cleaned_data['geotag']
            status = 'Sent'
            photoUrl = request.FILES['photoURL']
            req = Request(dateTime=dateTime, user_id=user_id, description=description,
                          geotag=geotag, status=status, photoURL=photoUrl)
            # is_anon = request.POST.get('anon', False)
            # if is_anon:
            #     animal.save()
            # else:
            #     if request.user.is_authenticated:
            #         animal.save()
            req.save()
            return HttpResponse('Заявка принята!')
        else:
            response = {}
            for k in form.errors:
                response[k] = form.errors[k][0]
            return HttpResponse({"Что-то не так:\n": response})

            return HttpResponseRedirect('?submitted=True')
    else:

        form = RequestForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'MainApp/add_request.html', {'form': form, 'submitted': submitted})


def add_animals(request):
    submitted = False
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            photoUrl = request.FILES['photoURL']
            color = form.cleaned_data['color']
            weight = form.cleaned_data['weight']
            special_signs = form.cleaned_data['special_signs']
            sort_animal = form.cleaned_data['sort_animal']
            gender = form.cleaned_data['gender']
            behavior = form.cleaned_data['behavior']
            animals = Animals(color=color, weight=weight, special_signs=special_signs,
                              sort_animal=sort_animal, gender=gender, behavior=behavior, photoUrl=photoUrl)
            animals.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = AnimalForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'MainApp/create_animals.html', {'form': form, 'submitted': submitted})


def check_list(request):
    animals = Animals.objects.order_by('weight')[:5]
    transfer = Transfer.objects.order_by('date_of_transfer')[:5]
    return render(request, 'MainApp/check_list.html', {'animals': animals, 'transfer' : transfer})



def about(request):
    return render(request, 'MainApp/about.html', {})


def pets(request):
    return render(request, 'MainApp/pets.html', {})


def news(request):
    return render(request, 'MainApp/news.html', {})


def act(request, op_id):
    transfer = get_object_or_404(Transfer, pk=op_id)
    return render(request, 'act.html', {'transfer': transfer})
