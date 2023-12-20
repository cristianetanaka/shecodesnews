# users/urls.py
from django.urls import path
from .views import CreateAccountView
from .views import profileview 
from users.views import UpdateProfileView

app_name = 'users'

urlpatterns = [
    path('createaccount/', CreateAccountView.as_view(), name='createAccount'),
    path('profile/<int:pk>/', profileview, name='profileview'),
    path('updateprofile/<int:pk>/', UpdateProfileView.as_view(), name='updateprofile'),
]