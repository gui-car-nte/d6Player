from django.urls import path
from . import views

app_name = 'scenes'

urlpatterns = [
    path('<int:scene_id>/', views.scene_detail, name = 'scene_detail'),
    path('create/', views.create_scene, name = 'create_scene'),
]