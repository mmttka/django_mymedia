from django.shortcuts import render
from topic.models import TopicModel
from tech.models import TechModel
from term.models import TermModel

def my_view(request):
    my_first_model = TopicModel.objects.all()
    my_second_model  = TechModel.objects.all()
    my_third_model  = TermModel.objects.all()

    context = {
        'first_list': my_first_model,
        'second_list': my_second_model,
        'third_list': my_third_model,
        
    }
    return render(request, 'home/home_list.html', context)
