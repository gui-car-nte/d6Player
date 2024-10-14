from django.shortcuts import render, redirect, get_object_or_404
from .scenes_forms import SceneForm, SceneLogUpdate
from .scenes_models import Scene
from campaigns.campaign_models import Campaign

def scene_detail(request, user_id, campaign_id, scene_id):
    scene = get_object_or_404(Scene, id = scene_id)
    characters = scene.characters.all()
    
    if request.method == 'POST':
        form = SceneLogUpdate(request.POST, instance = scene)
        if form.is_valid():
            form.save
    else: 
        form = SceneLogUpdate()
    return render(request, 'scenes/scene_detail.html', {
        'scene': scene,
        'form': form,
        'characters' : characters
    })

def create_scene(request, user_id, campaign_id):
    campaign = get_object_or_404(Campaign, id = campaign_id)
    if request.method == 'POST':
        form = SceneForm(request.POST)
        if form.is_valid():
            scene = form.save(commit = False)
            scene.campaign = campaign
            scene.save()
            return redirect(f'http://127.0.0.1:8000/campaigns/{user_id}/{campaign_id}/') # TODO replace hard-coded url
    else:
        form = SceneForm()
    return render(request, 'scenes/create_scene.html', {'form': form})
