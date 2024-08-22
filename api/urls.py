from rest_framework import routers
from .views import UserViewSet, CampaignViewSet, SceneSerializer, CharacterSerializer

app_name = 'api'
router = routers.DefaultRouter()
router.register('UserProfile', UserViewSet, 'user_api')
router.register('Campaign', CampaignViewSet, 'campaign_api')
router.register('Scene', SceneSerializer, 'scene_api')
router.register('Character', CharacterSerializer, 'character_api')
urlpatterns = router.urls