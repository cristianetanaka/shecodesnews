from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import CustomUser, UserProfile
from django.shortcuts import render
from .forms import CustomUserCreationForm


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


class UpdateProfileView(UpdateView):
    model = CustomUser
    template_name = 'users/updateprofile.html'
    success_url = reverse_lazy('users:profile')
