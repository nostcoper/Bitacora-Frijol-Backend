from rest_framework import serializers
from .models import (
    Achievement,
    Mission,
    Plant,
    Entry,
    EntryImage,
    PlantAchievement,
    UserAchievement,
    UserMission
)

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'

class EntryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryImage
        fields = '__all__'

class PlantAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantAchievement
        fields = '__all__'

class UserAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAchievement
        fields = '__all__'

class UserMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMission
        fields = '__all__'
