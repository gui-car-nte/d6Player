from django import forms
from .character_models import Character

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'appearance', 'personality', 'backstory', 'power_source', 'power_source_design', 'power_source_abilities']