from django.urls import path
from . import views

urlpatterns = [
    path('', views.scene_detail),
    path('create/', views.create_scene, name = 'create_scene'),
]