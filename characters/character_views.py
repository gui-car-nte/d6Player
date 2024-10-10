from django.shortcuts import render, redirect, get_object_or_404
from .character_forms import CharacterForm
from .character_models import Character
from campaigns.campaign_models import Campaign

def character_detail(request, user_id, campaign_id, character_id):
    character = get_object_or_404(Character, id = character_id)
    return render(request, 'characters/character_detail.html', {'character': character})

def create_character(request, user_id, campaign_id):
    campaign = get_object_or_404(Campaign, id = campaign_id)
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit = False)
            character.campaign = campaign
            character.save()
            return redirect(f'http://127.0.0.1:8000/campaigns/{user_id}/{campaign_id}/')
    else:
        form = CharacterForm()
    return render(request, 'characters/create_character.html', {'form': form})
