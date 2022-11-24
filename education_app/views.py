from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpRequest
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from .models import Work, Assessment
from .forms import WorkForm


# Create your views here.
class WorkListView(ListView):
    model = Work
    paginate_by = 2
    # Дальше только для удобства
    template_name = 'education_app/works_list.html'
    context_object_name = "works"


class WorkDetailView(DetailView):
    model = Work
    # Дальше только для удобства
    template_name = 'education_app/works_detail.html'
    context_object_name = "work"
    pk_url_kwarg = 'id'


class WorkCreateView(CreateView):
    model = Work
    form_class = WorkForm
    success_url = reverse_lazy('works-list')
    template_name_suffix = '_create'


class WorkDeleteView(DeleteView):
    model = Work
    success_url = reverse_lazy('works-list')
    template_name_suffix = '_delete'
    pk_url_kwarg = 'id'


class WorkUpdateView(UpdateView):
    model = Work
    form_class = WorkForm
    success_url = reverse_lazy('works-list')
    template_name_suffix = '_update'
    pk_url_kwarg = 'id'
