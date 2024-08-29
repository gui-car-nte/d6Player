from django.db import models
from campaigns.campaign_models import Campaign

class Scene(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete = models.CASCADE)
    name = models.CharField(max_length = 25)
    description = models.CharField(max_length = 75)
    action_log = models.TextField()

    def __str__(self):
        return self.name