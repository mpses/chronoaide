from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('text_to_schedule/', views.textToSchedule, name = 'text_to_schedule'),
]