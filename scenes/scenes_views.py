from django.shortcuts import render, redirect, get_object_or_404
from .scenes_forms import SceneForm
from .scenes_models import Scene
from campaigns.campaign_models import Campaign

def scene_detail(request, user_id, campaign_id, scene_id):
    scene = get_object_or_404(Scene, id = scene_id)
    return render(request, 'scenes/scene_detail.html', {'scene': scene})

def create_scene(request, user_id, campaign_id):
    campaign = get_object_or_404(Campaign, id = campaign_id)
    if request.method == 'POST':
        form = SceneForm(request.POST)
        if form.is_valid():
            scene = form.save(commit = False)
            scene.campaign = campaign
            scene.save()
            return redirect(f'http://127.0.0.1:8000/campaigns/{user_id}/{campaign_id}/')
    else:
        form = SceneForm()
    return render(request, 'scenes/create_scene.html', {'form': form})
