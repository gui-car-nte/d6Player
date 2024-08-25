from django.db import models
from home.models import UserProfile

class Campaign(models.Model):
    user = models.ForeignKey(UserProfile, on_delete = models.CASCADE, related_name='campaigns')
    campaign_name = models.CharField(max_length = 20)
    world_name = models.CharField(max_length = 20)
    campaign_description = models.CharField(max_length = 70)

    def __str__(self):
        return self.campaign_name