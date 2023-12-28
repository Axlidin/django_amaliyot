from django import forms
from .models import PostUserInfo

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = PostUserInfo
        fields = ['ism', 'familiya', 'telefon', 'email', 'xabar']