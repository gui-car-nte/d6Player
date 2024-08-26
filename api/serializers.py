from rest_framework import serializers
from home.models import UserProfile
from campaigns.campaign_models import Campaign
from scenes.scenes_models import Scene
from characters.character_models import Character

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'nickname')


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('__all__')


class SceneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scene
        fields = ('__all__')


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('__all__')