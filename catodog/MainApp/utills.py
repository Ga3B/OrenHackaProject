from django.shortcuts import render, get_object_or_404, redirect,reverse
from . import *

# детальное описание
class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, id):
        obj = get_object_or_404(self.model, id__iexact=id)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

# обновление
class ObjectUpdateMixin:
    model = None
    template = None
    model_form = None

    def get(self, request, id):
        obj = self.model.objects.get(id__iexact=id)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, id):
        obj = self.model.objects.get(id__iexact=id)
        bound_form = self.model_form(request.POST, instance=obj)
        if (bound_form.is_valid()):
            new_obj = bound_form.save()
            return redirect('')
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

# создание
class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect('')
        return render(request, self.template, context={'form': bound_form})

# удаление
class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, id):
        obj = self.model.objects.get(id__iexact=id)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, id):
        obj = self.model.objects.get(id__iexact=id)
        obj.delete()
        return redirect(reverse(self.redirect_url))
