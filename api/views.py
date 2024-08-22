from rest_framework import viewsets, permissions
from home.models import UserProfile
from campaigns.models import Campaign
from scenes.models import Scene
from characters.models import Character
from .serializers import UserSerializer, CampaignSerializer, SceneSerializer, CharacterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class CampaignViewSet():
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [permissions.AllowAny]

class SceneViewSet():
    queryset = Scene.objects.all()
    serializer_class = SceneSerializer
    permission_classes = [permissions.AllowAny]

class CharacterViewSet():
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.AllowAny]