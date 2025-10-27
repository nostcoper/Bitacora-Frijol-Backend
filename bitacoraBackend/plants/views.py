from rest_framework import viewsets
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
from .serializers import (
    AchievementSerializer,
    MissionSerializer,
    PlantSerializer,
    EntrySerializer,
    EntryImageSerializer,
    PlantAchievementSerializer,
    UserAchievementSerializer,
    UserMissionSerializer
)

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class EntryImageViewSet(viewsets.ModelViewSet):
    queryset = EntryImage.objects.all()
    serializer_class = EntryImageSerializer

class PlantAchievementViewSet(viewsets.ModelViewSet):
    queryset = PlantAchievement.objects.all()
    serializer_class = PlantAchievementSerializer

class UserAchievementViewSet(viewsets.ModelViewSet):
    queryset = UserAchievement.objects.all()
    serializer_class = UserAchievementSerializer

class UserMissionViewSet(viewsets.ModelViewSet):
    queryset = UserMission.objects.all()
    serializer_class = UserMissionSerializer
