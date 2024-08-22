from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create_campaign, name = 'create_campaign'),
    path('<str:username>/<str:campaign_name>', views.campaign_detail, name = 'campaign_detail'),
    path('<str:username>/<str:campaign_id>/characters', include('characters.urls')),
    path('<str:username>/<str:campaign_id>/scenes', include('scenes.urls')),
]
