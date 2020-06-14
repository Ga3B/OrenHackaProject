from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
import datetime


# def index(request):
#     return render(request, 'index.html', {'Test': "Placeholder"})


def help(request):
    return render(request, 'help.html', {})


def contacts(request):
    return render(request, 'contacts.html', {})


def donate(request):
    return render(request, 'donate.html', {})


@login_required()
def profile(request, action='no'):
    user = request.user
    if request.method == 'POST':
        if action == 'edit':
            user.first_name = request.POST.get('firstname')
            user.last_name = request.POST.get('lastname')
            try:
                user.full_clean()
            except ValidationError as e:
                return render(request, 'profile.html', {'user': user, 'error_message': e})
            else:
                user.save()
                return HttpResponseRedirect(reverse('profile', kwargs={'action': 'success'}))
    return render(request, 'profile.html', {'user': user, 'action': action})
