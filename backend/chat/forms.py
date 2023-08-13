from django import forms
from .models import Group, UserProfile


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'full_name']
