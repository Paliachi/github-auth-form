from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.accounts_app.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),

]
