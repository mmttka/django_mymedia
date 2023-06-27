from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TopicModel
from .consts import ITEM_PER_PAGE

class ListTopicView(ListView):
    template_name = 'topic/topic_list.html'
    model = TopicModel
    paginate_by = ITEM_PER_PAGE

class DetailTopicView(DetailView):
    template_name = 'topic/topic_detail.html'
    model = TopicModel

    