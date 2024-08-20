from django.db import models
from home.models import UserProfile

class Campaign(models.Model):
    user = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    campaign_name = models.CharField(max_length = 20)
    world_name = models.CharField(max_length = 20)
    campaign_description = models.CharField(max_length = 70)

