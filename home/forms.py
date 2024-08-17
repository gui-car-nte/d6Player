from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    nickname = forms.CharField(max_length = 30)

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'nickname')

    def save(self, commit = True):
        user = super().save(commit = False)
        user.nickname = self.cleaned_data['nickname']
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    nickname = forms.CharField(max_length = 30)

    class Meta:
        model = UserProfile
        fields = ('username', 'nickname')

    def save(self, commit = True):
        user = super().save(commit = False)
        user.nickname = self.cleaned_data['nickname']
        if commit:
            user.save()
        return user