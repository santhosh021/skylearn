from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from . import models



# Create your views here.

class LectureListView(LoginRequiredMixin, ListView):
    model = models.Lecture

@login_required
def list_article(request, title):
    article = models.LectureDetail.objects.filter(title=title)
    if models.LectureDetail.objects.filter(title=title):
        data = models.LectureDetail.objects.filter(title=title)[0]
        context = {'article':article, 'data':data}
    else:
        context = {'article':article}


    return render(request, 'lectures/lecture_detail.html', context)

@login_required
def detail_article(request, title, topic):
    title = title.lower()
    data = models.LectureDetail.objects.get(slug=topic)
    article = models.LectureDetail.objects.filter(title=title)

    context = {'data':data, 'article':article}
    return render(request, 'lectures/lecture_detail.html', context)
