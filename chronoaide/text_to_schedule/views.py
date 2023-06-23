from django.shortcuts import render
from django.http import HttpResponse
from .forms import EventForm
import requests
import json

# Create your views here.
def index(request):
    return HttpResponse('hello hello')

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            # フォームデータを取得
            text = form.cleaned_data['text']

            # GPT APIにリクエストを送信してデータを整形
            gpt_data = format_event_data(text)

            # Google Calendar APIと連携して予定を追加
            add_to_google_calendar(gpt_data)

            # 成功メッセージを表示
            message = "Event added to Google Calendar successfully!"
            return render(request, 'success.html', {'message': message})
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

GPT_API_URL = 'https://api.openai.com/v1/engines/davinci-codex/completions'
GPT_API_KEY = ''

def format_event_data(text):
    # GPT APIリクエストの実装
    instruction = ''
    prompt = f'{instruction}「{text}」'
    payload = {
        'prompt': prompt,
        'max_tokens': 100,
        'temperature': 0.7
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {GPT_API_KEY}'
    }
    response = requests.post(GPT_API_URL, data = json.dumps(payload), headers = headers)
    gpt_response = response.json()
    formatted_data = gpt_response['choices'][0]['message']['content'].strip(';')
    return formatted_data

def add_to_google_calendar(event_data):
    # Google Calendar APIリクエストの実装
    # ...
    pass