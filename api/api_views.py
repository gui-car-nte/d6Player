from rest_framework import viewsets, permissions
from home.models import UserProfile
from campaigns.campaign_models import Campaign
from scenes.scenes_models import Scene
from characters.character_models import Character
from .serializers import UserSerializer, CampaignSerializer, SceneSerializer, CharacterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)


class SceneViewSet(viewsets.ModelViewSet):
    queryset = Scene.objects.all()
    serializer_class = SceneSerializer
    permission_classes = [permissions.AllowAny]


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.AllowAny]