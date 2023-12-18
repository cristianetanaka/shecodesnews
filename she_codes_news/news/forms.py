from django import forms
from django.forms import ModelForm
from .models import NewsStory

class Storyform(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'image_url', 'content']
        widgets = { 
            'pub_date': forms.DateTimeInput(
            format= '%d/%m/%Y',
            attrs={
                'class':'form-control',
                'placeholder':'Select a date',
                'type':'datetime-local'
                }
            ),
        }