from django import forms
from .models import Scene

class SceneForm(forms.ModelForm):
    class Meta:
        model = Scene
        fields = ['name', 'description', 'action_log']