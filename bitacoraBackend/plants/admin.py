from django.contrib import admin
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

admin.site.register(Achievement)
admin.site.register(Mission)
admin.site.register(Plant)
admin.site.register(Entry)
admin.site.register(EntryImage)
admin.site.register(PlantAchievement)
admin.site.register(UserAchievement)
admin.site.register(UserMission)
