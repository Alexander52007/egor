from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
]