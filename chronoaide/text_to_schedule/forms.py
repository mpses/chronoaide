from django import forms

class EventForm(forms.Form):
    text = forms.CharField(label = 'text')