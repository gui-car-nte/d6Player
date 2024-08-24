from rest_framework import routers
from .views import UserViewSet, CampaignViewSet, SceneViewSet, CharacterViewSet

app_name = 'api'
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename = 'user')
router.register(r'campaigns', CampaignViewSet, basename = 'campaign')
router.register(r'scenes', SceneViewSet, basename = 'scene')
router.register(r'characters', CharacterViewSet, basename = 'character')
urlpatterns = router.urls