from django.urls import path
from . import scenes_views

app_name = 'scenes'

urlpatterns = [
    path('<int:scene_id>/', scenes_views.scene_detail, name = 'scene_detail'),
    path('create/', scenes_views.create_scene, name = 'create_scene'),
]