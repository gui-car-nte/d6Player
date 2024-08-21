from django.shortcuts import render, redirect, get_object_or_404
from .forms import CampaignForm
from .models import Campaign
from scenes.models import Scene
from home.models import UserProfile
from utils import get_db_handle, MongoClient

def campaign_detail(request, username, campaign_name):
    user = get_object_or_404(UserProfile, username = username)
    campaign = get_object_or_404(Campaign, user = user, campaign_name = campaign_name)
    scenes = Scene.objects.filter(campaign = campaign)
    return render(request, 'campaigns/campaign_detail.html', {'campaign': campaign, 'scenes': scenes})

def create_campaign(request):
    db_handle, client = get_db_handle(
        # aqui va la URI de mongo
        db_name = "d6player",
        host = "localhost",
        port = 27017,
        )
    collection = db_handle['campaigns']
    
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign_data = form.cleaned_data
            campaign_data['user'] = request.user.username
            collection.insert_one(campaign_data)
            return redirect('home:home')
    else:
        form = CampaignForm()
    
    return render(request, 'campaigns/create_campaign.html', {'form': form})