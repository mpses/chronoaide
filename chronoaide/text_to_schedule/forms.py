from django import forms

class EventForm(forms.Form):
    title = forms.CharField(label = 'Title', max_length = 255)
    start_time = forms.DateTimeField(label = 'Start Time')
    end_time = forms.DateTimeField(label = 'End Time')