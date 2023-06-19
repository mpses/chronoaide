from django.shortcuts import render
from django.http import HttpResponse
from .forms import EventForm
import requests

# Create your views here.
def index(request):
    return HttpResponse('hello hello')

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            # フォームデータを取得
            title = form.cleaned_data['title']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']

            # GPT APIにリクエストを送信してデータを整形
            gpt_data = format_event_data(title, start_time, end_time)

            # Google Calendar APIと連携して予定を追加
            add_to_google_calendar(gpt_data)

            # 成功メッセージを表示
            message = "Event added to Google Calendar successfully!"
            return render(request, 'success.html', {'message': message})
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

def format_event_data(title, start_time, end_time):
    # GPT APIリクエストの実装
    # ...
    pass

def add_to_google_calendar(event_data):
    # Google Calendar APIリクエストの実装
    # ...
    pass