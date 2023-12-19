from django.urls import reverse_lazy
#from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import CustomUser, UserProfile
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import render, reverse
from .forms import CustomUserCreationForm, CustomUserChangeForm, UserProfile 


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'
#form_valid override to create a user profile for newly create user
    def form_valid(self, form):
        #form.instance.author = self.request.user
        response = super() .form_valid(form)
        UserProfile.objects.create(user=self.object)
        return response


@login_required # user must be login to access view
              
def profileview (request,pk):
    user = CustomUser.objects.get(pk=pk)
    #user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'users/profile.html', {'UserProfile' : UserProfile})

@method_decorator(login_required, name='dispatch')

class UpdateProfileView(UpdateView):
    model = UserProfile
    form_class = CustomUserChangeForm
    template_name = 'users/updateprofile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user.userprofile

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error updating your profile. Please correct the errors below.')
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse('users:profileview', kwargs={'pk' : self.object.pk})


