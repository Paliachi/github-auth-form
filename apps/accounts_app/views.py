from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile
from .forms import ProfileForm


def github_login(request):
    return render(request, 'github_login.html', {})


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


# @login_required(login_url='login')
class AccountProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}
        try:
            profile = Profile.objects.get(user_id=request.user.id)
            context['profile'] = profile
        except ObjectDoesNotExist:
            pass

        return render(request, 'account_profile.html', context)


# @login_required(login_url='login')
class ProfileFormView(View):
    def get(self, request, *args, **kwargs):
        instance = Profile.objects.get_or_create(user=request.user)
        form = ProfileForm(instance=instance[0])
        context = {'form': form}
        return render(request, 'profile_form.html', context)

    def post(self, request, *args, **kwargs):
        instance = Profile.objects.get(user=request.user)
        form = ProfileForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()

        return render(request, 'profile_form.html', {'form': form})

