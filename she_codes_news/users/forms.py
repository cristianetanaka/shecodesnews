# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UserProfile

#Creation of New User
class CustomUserCreationForm(UserCreationForm):
    bio = forms.CharField(max_length=500, required = True, help_text="What's your story?")
    class Meta:        
        model = CustomUser        
        fields = ['username', 'email', 'bio']
        
#create a user profile form(optional)

class UserProfileForm(forms.ModelForm):
    class Meta:        
        model = UserProfile        
        #fields = ['bio', 'profile_picture'] #bio is user's biography and avatar user's profile picture
        fields = ['bio'] #bio is user's biography 
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:        
        model = CustomUser        
        fields = ['username', 'email', 'bio']
        
