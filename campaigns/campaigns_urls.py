from django.urls import path, include
from . import campaign_views

app_name = 'campaigns'

urlpatterns = [
    path('create/', campaign_views.create_campaign, name = 'create_campaign'),
    path('<int:user_id>/<int:campaign_id>/', campaign_views.campaign_detail, name = 'campaign_detail'),
    path('<int:user_id>/<int:campaign_id>/characters/', include('characters.characters_urls')),
    path('<int:user_id>/<int:campaign_id>/scenes/', include('scenes.scenes_urls')),
]