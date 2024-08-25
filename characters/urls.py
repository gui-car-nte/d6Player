from django.urls import path
from . import views

urlpatterns = [
    # path('', views.character_detail), # TODO this view does not currently exist
    path('create/', views.create_character, name = 'create_character'),
]
