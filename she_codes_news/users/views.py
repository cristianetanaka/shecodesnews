from typing import Any
from django.views import generic
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CreateAccountView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class AccountView(generic.DetailView):
    model = CustomUser
    template_name = 'users/account.html'
    context_object_name = 'account'

    def get_object(self, queryset=None):
        return self.request.user

class UpdateAccountView(generic.UpdateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/updateaccount.html'

    def get_object(self, queryset=None):
        return self.request.user

class DeleteAccountView(generic.DeleteView):
    model = CustomUser
    template_name = 'users/deleteaccount.html'
    success_url = reverse_lazy('news:index')