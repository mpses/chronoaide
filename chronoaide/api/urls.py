from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('text_to_schedule/', views.text_formatter_api, name = 'text_to_schedule'),
]