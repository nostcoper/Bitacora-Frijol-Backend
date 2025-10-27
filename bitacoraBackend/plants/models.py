from django.db import models
from django.conf import settings

# ---------------- Achievement ----------------
class Achievement(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'achievement'

    def __str__(self):
        return self.name


# ---------------- Mission ----------------
class Mission(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    points = models.IntegerField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'mission'

    def __str__(self):
        return self.title


# ---------------- Plant ----------------
class Plant(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='plants',
        db_column='user_id'
    )
    name = models.CharField(max_length=255)
    image_url = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'plant'
        indexes = [
            models.Index(fields=['user'], name='idx_plant_user'),
        ]

    def __str__(self):
        return f"{self.name} - {self.user.username}"


# ---------------- Entry ----------------
class Entry(models.Model):
    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE,
        related_name='entries',
        db_column='plant_id'
    )
    height = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(null=True, blank=True)
    recorded_at = models.DateTimeField()

    class Meta:
        db_table = 'entry'
        indexes = [
            models.Index(fields=['plant', 'recorded_at'], name='idx_entry_plant_ts'),
        ]

    def __str__(self):
        return f"Entry for {self.plant.name} - {self.height}cm"


# ---------------- EntryImage ----------------
class EntryImage(models.Model):
    entry = models.ForeignKey(
        Entry,
        on_delete=models.CASCADE,
        related_name='images',
        db_column='entry_id'
    )
    image_url = models.TextField()

    class Meta:
        db_table = 'entry_image'
        indexes = [
            models.Index(fields=['entry'], name='idx_entry_image_entry'),
        ]

    def __str__(self):
        return f"Image for entry {self.entry.id}"


# ---------------- PlantAchievement ----------------
class PlantAchievement(models.Model):
    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE,
        related_name='achievements',
        db_column='plant_id'
    )
    achievement = models.ForeignKey(
        Achievement,
        on_delete=models.CASCADE,
        related_name='plant_achievements',
        db_column='achievement_id'
    )
    awarded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'plant_achievement'
        indexes = [
            models.Index(fields=['plant'], name='idx_pla_achv_plant'),
            models.Index(fields=['achievement'], name='idx_pla_achv_achv'),
        ]

    def __str__(self):
        return f"{self.plant.name} - {self.achievement.name}"


# ---------------- UserAchievement ----------------
class UserAchievement(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='achievements',
        db_column='user_id'
    )
    achievement = models.ForeignKey(
        Achievement,
        on_delete=models.CASCADE,
        related_name='user_achievements',
        db_column='achievement_id'
    )
    awarded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_achievement'
        indexes = [
            models.Index(fields=['user'], name='idx_usr_achv_user'),
            models.Index(fields=['achievement'], name='idx_usr_achv_achv'),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.achievement.name}"


# ---------------- UserMission ----------------
class UserMission(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='missions',
        db_column='user_id'
    )
    mission = models.ForeignKey(
        Mission,
        on_delete=models.CASCADE,
        related_name='user_missions',
        db_column='mission_id'
    )
    completed_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_mission'
        indexes = [
            models.Index(fields=['user'], name='idx_user_mission_user'),
            models.Index(fields=['mission'], name='idx_user_mission_mission'),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.mission.title}"
