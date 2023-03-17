from social_django.views import disconnect

from django.urls import path

from .views import (
    homepage,
    github_login,
    logout_view,
    delete_user,
    AccountProfileView,
    ProfileFormView
)


urlpatterns = [
    path('', homepage, name='homepage'),
    path('login', github_login, name='login'),
    path('logout', logout_view, name='logout'),
    path('delete/user/', delete_user, name='deleteUser'),
    # path('social-auth/complete/github/accounts/github/callback/', github_login, name='callback'),
    path('profile/', AccountProfileView.as_view(), name='profile'),
    path('profile-form/', ProfileFormView.as_view(), name='profileForm'),
]
