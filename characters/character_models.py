from django.db import models
from scenes.scenes_models import Scene
from campaigns.campaign_models import Campaign
from config import CHARACTER_STATS, POWER_SOURCE_STATS, STATS_RANKS

class Character(models.Model):
    STAND_USER = "Stand User"
    HAMON_WARRIOR = "Hamon Warrior"
    VAMPIRE = "Vampire"
    SPIN_MASTER = "Spin Master"
    ARMED_PHENOMENON = "Armed Phenomenon"
    NO_POWER_SOURCE = "No Power Source"

    CHARACTER_POWER_SOURCES = [
        (STAND_USER, "Stand User"),
        (HAMON_WARRIOR, "Hamon Warrior"),
        (VAMPIRE, "Vampire"),
        (SPIN_MASTER, "Spin Master"),
        (ARMED_PHENOMENON, "Armed Phenomenon"),
        (NO_POWER_SOURCE, "No Power Source"),
    ]

    scene = models.ManyToManyField(Scene)
    campaign = models.ForeignKey(Campaign, on_delete = models.CASCADE)
    name = models.CharField(max_length = 30, blank = False)
    appearance = models.CharField(max_length = 100, blank = True)
    personality = models.CharField(max_length = 100, blank = True)
    backstory = models.CharField(max_length = 300, blank = True)
    power_source = models.CharField(max_length = 30, choices = CHARACTER_POWER_SOURCES, default = NO_POWER_SOURCE)
    power_source_design = models.CharField(max_length = 100, blank = True)
    power_source_abilities = models.CharField(max_length = 200, blank = True)
    

class CharacterStat(models.Model):
    character = models.ForeignKey(Character, on_delete = models.CASCADE, related_name = 'user_stats')
    stat_name = models.CharField(max_length = 10, choices = [(stat, stat) for stat in CHARACTER_STATS])
    stat_rank = models.CharField(max_length = 1, choices = STATS_RANKS.items())

    def __str__(self):
        # return f"{self.stat_name}: {self.get_stat_rank_display()}" # TODO make the method to get specific rank
        pass

class PowerSourceStat(models.Model):
    character = models.ForeignKey(Character, on_delete = models.CASCADE, related_name = 'power_stats')
    stat_name = models.CharField(max_length = 10, choices = [(stat, stat) for stat in POWER_SOURCE_STATS])
    stat_rank = models.CharField(max_length = 1, choices = STATS_RANKS.items())

    def __str__(self):
        # return f"{self.stat_name}: {self.get_stat_rank_display()}" # TODO make the method to get specific rank
        pass