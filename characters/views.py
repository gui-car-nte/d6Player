from django.shortcuts import render, redirect, get_object_or_404
from .forms import CharacterForm
from .models import Character
from campaigns.models import Campaign

def create_character(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.campaign = campaign
            character.save()
            return redirect('campaign_detail', username=campaign.user.username, campaign_name=campaign.campaign_name)
    else:
        form = CharacterForm()
    return render(request, 'characters/create_character.html', {'form': form})
