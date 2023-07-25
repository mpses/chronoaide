from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('text_to_schedule/', views.text_formatter_api, name = 'text_to_schedule'),
    path('add_to_google_calendar/', views.add_to_google_calendar_api, name = 'add_to_google_calendar'),
]