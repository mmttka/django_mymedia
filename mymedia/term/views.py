from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TermModel
from .consts import ITEM_PER_PAGE

class ListTermView(ListView):
    template_name = 'term/term_list.html'
    model = TermModel
    paginate_by = ITEM_PER_PAGE

    

class DetailTermView(DetailView):
    template_name = 'term/term_detail.html'
    model = TermModel

    