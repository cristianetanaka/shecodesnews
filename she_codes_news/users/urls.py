# users/urls.py
from django.urls import path
from .views import CreateAccountView, profileView
#from .views import profileView,edit_profile
from .import views

app_name = 'users'

urlpatterns = [
    path('createaccount/', CreateAccountView.as_view(), name='createAccount'),
    path('profile/', profileView, name='profileView'),
    path('updateprofile/', views.UpdateProfileView, name='update_profile'),
]