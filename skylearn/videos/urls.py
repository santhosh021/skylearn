from django.urls import path
from . import views

app_name = 'videos'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='courses'),
    path('<slug:course_name_slug>/', views.list_videos, name='videolist'),
    path('<slug:course_name_slug>/<slug:video_name_slug>/', views.detail_videos, name='videodetail'),
]
