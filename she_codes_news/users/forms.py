# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

#Creation of New User
class CustomUserCreationForm(UserCreationForm):
    bio = forms.CharField(max_length=500, required = True, help_text="What's your story?") 
    
    class Meta:        
        model = CustomUser        
        fields = ['username', 'email', 'bio']

