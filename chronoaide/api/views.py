from django.shortcuts import render
from django.http import HttpResponse

# import from parent directory
import sys
sys.path.append('../')
from text_to_schedule import views as tts_views

# Create your views here.
def index(request):
    pass

def textToSchedule(request):
    return tts_views.format_event_data(request.POST['text'])