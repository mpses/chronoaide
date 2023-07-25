from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# import from parent directory
import sys
sys.path.append('../')
from text_to_schedule import views as tts_views

# Create your views here.
def index(request):
    pass

@api_view(['POST'])
def text_formatter_api(request):
    raw_text = request.data['text']
    # schedule = tts_views.format_event_data(raw_text)
    # for example
    schedule = {'schedules':[
        {
            'name': '太郎君誕生日会',
            'start': '2023-04-24 10:00',
            'end': None,
            'place': '代々木公園',
            'detail': 'プレゼントを持ってくること。'
        },{
            'name': '東京大学入学式',
            'start': '2023-04-03 10:00',
            'end': '2023-04-03 12:00',
            'place': '日本武道館',
            'detail': '入学式のため、スーツを着ていくこと。'
        }
    ]}
    return Response(schedule)

@api_view(['POST'])
def add_to_google_calendar_api(request):
    schedules = request.data['schedules']
    token = request.data['token']
    try:
        tts_views.add_to_google_calendar(schedules)
        return Response({'message': 'success'}, status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': str(e)}, status = status.HTTP_400_BAD_REQUEST)