from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('profile')
    return redirect('login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_redirect, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
    path('schedule/', include('schedule.urls')),
]