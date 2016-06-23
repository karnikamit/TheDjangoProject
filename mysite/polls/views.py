# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    questions = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context=questions)


def detail(request, question_id):
    return HttpResponse("you're reading question ID: %d " % int(question_id))


def results(request, question_id):
    return HttpResponse("you're reading results for %d" % int(question_id))


def vote(request, question_id):
    return HttpResponse("you're voting to question id: %d" % int(question_id))

