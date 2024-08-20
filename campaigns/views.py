from django.shortcuts import render, get_object_or_404
from .models import Campaign
from home.models import UserProfile

def campaign_detail(request, username, campaign_name):
    user = get_object_or_404(UserProfile, username = username)
    campaign = get_object_or_404(Campaign, user = user, campaign_name = campaign_name)
    return render(request, 'campaigns/campaign_detail.html', {'campaign': campaign})
