from django.urls import path
from . import views

app_name = 'lectures'

urlpatterns = [
    path('', views.LectureListView.as_view(), name='lecture'),
    path('<slug:title>/', views.list_article, name='articlelist'),
    path('<slug:title>/<slug:topic>/', views.detail_article, name='articledetail'),
]
