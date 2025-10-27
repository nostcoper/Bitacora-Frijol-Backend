from rest_framework.routers import DefaultRouter
from .views import (
    AchievementViewSet,
    MissionViewSet,
    PlantViewSet,
    EntryViewSet,
    EntryImageViewSet,
    PlantAchievementViewSet,
    UserAchievementViewSet,
    UserMissionViewSet
)

router = DefaultRouter()
router.register(r'achievements', AchievementViewSet)
router.register(r'missions', MissionViewSet)
router.register(r'plants', PlantViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'entry-images', EntryImageViewSet)
router.register(r'plant-achievements', PlantAchievementViewSet)
router.register(r'user-achievements', UserAchievementViewSet)
router.register(r'user-missions', UserMissionViewSet)

urlpatterns = router.urls
