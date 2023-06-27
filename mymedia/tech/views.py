from typing import Any, Optional
from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TechModel
from .consts import ITEM_PER_PAGE
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .forms import TechForm
from django.contrib.auth.decorators import login_required



class ListTechView(ListView):
    template_name = 'tech/tech_list.html'
    model = TechModel
    paginate_by = ITEM_PER_PAGE


class DetailTechView(DetailView):
    template_name = 'tech/tech_detail.html'
    model = TechModel


class CreateTechView(LoginRequiredMixin, CreateView):
    template_name = 'tech/tech_create.html'
    model = TechModel
    fields = ('title', 'text', 'thumbnail')
    success_url = reverse_lazy('list-tech')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)



class DeleteTechView(LoginRequiredMixin, DeleteView):
    template_name = 'tech/tech_delete.html'
    model = TechModel
    success_url = reverse_lazy('list-tech')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied
        
        return obj


class UpdateTechView(LoginRequiredMixin, UpdateView):
    template_name = 'tech/tech_update.html'
    model = TechModel
    fields = ('title', 'text', 'thumbnail')
    success_url = reverse_lazy('list-tech')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied
        
        return obj
    
    def get_success_url(self):
        return reverse('detail-tech', kwargs={'pk':self.object.id})
    

@login_required
def add_form(request):

    if request.method == "POST":
        form = TechForm(request.POST, request.FILES)

        if form.is_valid():
            tech = form.save(commit=False)
            tech.user = request.user
            tech.save()
            return redirect('list-tech')

    else:
        form = TechForm()

    return render(request, 'tech/tech_create.html', {'form': form })