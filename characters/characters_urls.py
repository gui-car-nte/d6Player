from django.urls import path
from . import character_views

app_name = 'characters'

urlpatterns = [
    path('<int:character_id>', character_views.character_detail, name = 'character_detail'),
    path('create/', character_views.create_character, name = 'create_character'),
]
