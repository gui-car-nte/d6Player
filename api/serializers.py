from rest_framework import serializers
from home.models import UserProfile
from campaigns.models import Campaign
from scenes.models import Scene
from characters.models import Character

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'nickname')


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('campaign_name', 'world_name', 'campaign_description')


class SceneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scene
        fields = ('name', 'description', 'action_log')


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('name', 'appearance', 'personality', 'backstory', 'power_source', 'power_source_design', 'power_source_abilities')