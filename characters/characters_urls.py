from django.urls import path
from . import character_views

urlpatterns = [
    path('', character_views.character_detail, name = 'character_detail'),
    path('create/', character_views.create_character, name = 'create_character'),
]
