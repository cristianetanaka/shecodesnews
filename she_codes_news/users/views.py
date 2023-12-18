from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm, UserProfileForm 


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'
#form_valid override to create a user profile for newly create user
    def form_valid(self, form):
        #form.instance.author = self.request.user
        response = super() .form_valid(form)
        UserProfileForm.objects.create(user=self.object)
        return response


@login_required # user must be login to access view
              
def profileView(request):
    user_profile = UserProfileForm.objects.get(user=request.user)
    return render(request, 'profile.html', {'user_profile' : user_profile})

@login_required

class UpdateProfileView(View):
    template_name = 'updateprofile.html'

    def get(self, request, *args, **kwargs):
        user_form = CustomUserChangeForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request, *args, **kwargs):
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Error updating your profile. Please correct the errors below.')
            return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})



