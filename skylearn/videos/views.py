from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.
class CourseListView(LoginRequiredMixin, ListView):
    model = models.Course

@login_required
def list_videos(request, course_name_slug):
    vidlist = models.Videos.objects.filter(video_course=course_name_slug)
    context = {'vidlist':vidlist}
    return render(request, 'videos/video_list.html', context)

@login_required
def detail_videos(request, course_name_slug, video_name_slug):
    viddetail = models.Videos.objects.get(video_name_slug=video_name_slug)
    context = {'viddetail': viddetail}
    return render(request, 'videos/video_detail.html', context)
