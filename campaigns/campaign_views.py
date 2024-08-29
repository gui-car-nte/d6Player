from django.shortcuts import render, redirect, get_object_or_404
from .campaign_forms import CampaignForm
from .campaign_models import Campaign
from scenes.scenes_models import Scene
from characters.character_models import Character
from home.models import UserProfile

def campaign_detail(request, user_id, campaign_id):
    user = get_object_or_404(UserProfile, id = user_id)
    campaign = get_object_or_404(Campaign, user = user, id = campaign_id)
    scenes = Scene.objects.filter(campaign = campaign)
    characters = Character.objects.filter(campaign = campaign)
    return render(request, 'campaigns/campaign_detail.html', {'campaign': campaign, 'scenes': scenes, 'characters': characters})

def create_campaign(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign_data = form.cleaned_data
            campaign_data['user'] = request.user
            campaign = Campaign(**campaign_data) 
            campaign.save() 
            return redirect('home')
    else:
        form = CampaignForm()

    return render(request, 'campaigns/create_campaign.html', {'form': form})