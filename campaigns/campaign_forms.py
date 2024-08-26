from django import forms
from .campaign_models import Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['campaign_name', 'world_name', 'campaign_description']