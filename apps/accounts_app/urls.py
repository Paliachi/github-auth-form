from django.urls import path

from .views import github_login, AccountProfileView, logout_view, ProfileFormView


urlpatterns = [
    path('login', github_login, name='login'),
    path('logout', logout_view, name='logout'),
    # path('social-auth/complete/github/accounts/github/callback/', github_login, name='callback'),
    path('profile/', AccountProfileView.as_view(), name='profile'),
    path('profile-form/', ProfileFormView.as_view(), name='profileForm'),
]
