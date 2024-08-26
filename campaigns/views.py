from django.shortcuts import render, redirect, get_object_or_404
from .forms import CampaignForm
from .models import Campaign
from scenes.models import Scene
from characters.models import Character
from home.models import UserProfile

def campaign_detail(request, username, campaign_name):
    user = get_object_or_404(UserProfile, username = username)
    campaign = get_object_or_404(Campaign, user = user, campaign_name = campaign_name)
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