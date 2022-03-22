from django.urls import path
from . import views

app_name = 'exercises'

urlpatterns = [
    path('', views.QuizListView.as_view(), name='category'),
    path('<str:category>', views.quiz_list, name='quiz_list'),
]
