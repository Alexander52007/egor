from django import forms
from django.contrib.auth.models import User
from .models import Profile
from schedule.models import Group

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'role', 'group']