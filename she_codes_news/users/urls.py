# users/urls.py
from django.urls import path
from .views import CreateAccountView, AccountView,UpdateAccountView,DeleteAccountView



app_name = 'users'

urlpatterns = [
    path('createaccount/', CreateAccountView.as_view(), name='createAccount'),
    path('account/<int:pk>/', AccountView.as_view(), name='accountview'),
    path('updateaccount/<int:pk>/', UpdateAccountView.as_view(), name='updateaccount'),
    path('deleteaccount/<int:pk>/', DeleteAccountView.as_view(), name='deleteaccount'),
]