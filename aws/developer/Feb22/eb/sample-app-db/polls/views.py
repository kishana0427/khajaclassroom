import imp
from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Question, Choice
# Create your views here.

class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name = 'latest_questions_list'

    def get_queryset(self) :
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        ). order_by('-pub_date')
