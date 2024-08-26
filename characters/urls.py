from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_detail, name = 'character_detail'),
    path('create/', views.create_character, name = 'create_character'),
]
