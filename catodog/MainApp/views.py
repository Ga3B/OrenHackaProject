from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from MainApp.utills import *
from .models import Request, Animals, Visitor, Transfer, Status, Lost_animals
from .forms import RequestForm, AnimalForm, CatcherForm, Lost_animalsForm
import datetime


def index(request):
    return render(request, 'MainApp/index.html')


def detail(request, animal_id):
    animal = get_object_or_404(Animals, pk=animal_id)
    return render(request, 'MainApp/detail.html', {'animal': animal})


class AnimalDetail(ObjectDetailMixin, View):
    model = Animals
    template = 'MainApp/detail_animals.html'


def requests_all(request):
    req = Request.objects.all()
    return render(request, 'MainApp/detail_request.html', {'request': req})


def add_request(request):
    submitted = False
    if request.method == 'POST':

        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():

            dateTime = datetime.datetime.now()
            user_id = request.user
            description = form.cleaned_data['description']
            geotag = form.cleaned_data['geotag']
            status = get_object_or_404(Status, pk=1)
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
            return HttpResponseRedirect('?submitted=True')
        # else:
        #     response = {}
        #     for k in form.errors:
        #         response[k] = form.errors[k][0]
        #     return HttpResponse({"Что-то не так:\n": response})

            # return HttpResponseRedirect('?submitted=True')
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
            photoUrl = request.FILES['photoUrl']
            color = form.cleaned_data['color']
            weight = form.cleaned_data['weight']
            special_signs = form.cleaned_data['special_signs']
            sort_animal = form.cleaned_data['sort_animal']
            gender = form.cleaned_data['gender']
            behavior = form.cleaned_data['behavior']
            chip = form.cleaned_data['chip']
            animals = Animals(color=color, weight=weight, special_signs=special_signs,
                              sort_animal=sort_animal, gender=gender, behavior=behavior, PhotoUrl=photoUrl,
                              chip=chip)
            animals.save()
            return HttpResponse('Заявка принята!')
        else:
            response = {}
            for k in form.errors:
                response[k] = form.errors[k][0]
            return HttpResponse({"Что-то не так:\n": response})

            return HttpResponseRedirect('?submitted=True')
    else:

        form = AnimalForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'MainApp/create_animals.html', {'form': form, 'submitted': submitted})


def check_list(request):
    animals = Animals.objects.order_by('weight')[:5]
    transfer = Transfer.objects.order_by('date_of_transfer')[:5]
    return render(request, 'MainApp/check_list.html', {'animals': animals, 'transfer': transfer})


def about(request):
    return render(request, 'MainApp/about.html', {})


def pets(request):
    return render(request, 'MainApp/pets.html', {})


def news(request):
    return render(request, 'MainApp/news.html', {})

#
# def act(request, op_id):
#     transfer = get_object_or_404(Transfer, pk=transfer_id)
#     animal = get_object_or_404(Animals, pk=animal_id)
#     return render(request, 'act.html', {'transfer': transfer, 'animal': animal})


class TransferDetail(ObjectDetailMixin, View):
    model = Transfer
    template = 'MainApp/detail_transfer.html'


def catcher(request):
    submitted = False
    if request.method == 'POST':
        form = CatcherForm(request.POST, request.FILES)
        if form.is_valid():
            doc = request.FILES['doc']
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            inn = form.cleaned_data['inn']

        #     return HttpResponse('Заявка принята!')
        # else:
        #     response = {}
        #     for k in form.errors:
        #         response[k] = form.errors[k][0]
        #     return HttpResponse({"Что-то не так:\n": response})

        #     return HttpResponseRedirect('?submitted=True')
    else:

        form = CatcherForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'MainApp/catcher.html', {'form': form, 'submitted': submitted})


def lost_animals(request):
    submitted = False
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            photoUrl = request.FILES['photoUrl']
            color = form.cleaned_data['color']
            weight = form.cleaned_data['weight']
            special_signs = form.cleaned_data['special_signs']
            sort_animal = form.cleaned_data['sort_animal']
            gender = form.cleaned_data['gender']
            behavior = form.cleaned_data['behavior']
            chip = form.cleaned_data['chip']
            animals = Animals(color=color, weight=weight, special_signs=special_signs,
                              sort_animal=sort_animal, gender=gender,
                              behavior=behavior, PhotoUrl=photoUrl, chip=chip)
            animals.save()
            lost_form = Lost_animalsForm(request.POST)
            if lost_form.is_valid():
                userid = request.user
                date = datetime.datetime.now()
                animals_id = Animals.objects.get(color=color, weight=weight, special_signs=special_signs,
                                                 sort_animal=sort_animal, gender=gender, behavior=behavior, chip=chip)
                lost_animal = Lost_animals(
                    user_id=userid, date=date, animal_id=animals_id)
                lost_animal.save()

            return HttpResponse('Заявка принята!')
        else:
            response = {}
            for k in form.errors:
                response[k] = form.errors[k][0]
            return HttpResponse({"Что-то не так:\n": response})

            return HttpResponseRedirect('?submitted=True')
    else:

        form = AnimalForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'MainApp/create_animals.html', {'form': form, 'submitted': submitted})


def changestatus(request, req_id, stat_id):
    if request.method == 'POST':
        req = Request.objects.get(pk=req_id)
        st = Status.objects.get(pk=stat_id)
        req.status = st
        req.save()
        return HttpResponseRedirect('?submitted=True')
