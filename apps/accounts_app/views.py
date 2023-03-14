import requests
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.views.generic.edit import FormView

from .models import Account, Profile
from .forms import ProfileForm


def github_login(request):
    return render(request, 'github_login.html', {})


class AccountProfileView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        try:
            profile = Profile.objects.get(user_id=request.user.id)
            context['profile'] = profile
        except ObjectDoesNotExist:
            pass

        return render(request, 'account_profile.html', context)


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


def logout_view(request):
    logout(request)
    return redirect('login')


