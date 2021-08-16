from django.shortcuts import render
from django.views.generic.list import ListView, View
from .models import Notebook, Smartphone, Televizor, Konditsaner, Muzlatkich, Gaz
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'layout.html')

# @login_required
class NotebookPro(ListView):
    model = Notebook
    template_name = 'main/notebook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Notebook.objects.all()

        return context

# @login_required
class TelevizorPro(ListView):
    model = Televizor
    template_name = 'main/televizor.html'

    def get_context_data(self, **kwargs):
        context = super(TelevizorPro, self).get_context_data(**kwargs)
        context['object_tele'] = Televizor.objects.all()
        return context
# @login_required
class KonditsanerPro(ListView):
    model = Konditsaner
    template_name = "main/konditsaner.html"
    def get_context_data(self, **kwargs):
        context = super(KonditsanerPro, self).get_context_data(**kwargs)
        context['object_kon'] = Konditsaner.objects.all()
        return context


# @login_required
class SmartPhonePro(ListView):
    model = Smartphone
    template_name = 'main/smatphone.html'
    def get_context_data(self, **kwargs):
        context = super(SmartPhonePro, self).get_context_data(**kwargs)
        context['object_smart'] = Smartphone.objects.all()
        return context


# @login_required
class GazPro(ListView):
    model = Gaz
    template_name = 'main/gaz_plita.html'
    def get_context_data(self, **kwargs):
        context = super(GazPro, self).get_context_data(**kwargs)
        context['object_gaz'] = Gaz.objects.all()
        return context