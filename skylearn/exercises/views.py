from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
class QuizListView(LoginRequiredMixin, ListView):
    model = Category

@login_required
def quiz_list(request, category):
    quizlist = Question.objects.filter(category=category)
    context = {'quizlist':quizlist}
    return render(request, 'exercises/quizlist.html', context)
