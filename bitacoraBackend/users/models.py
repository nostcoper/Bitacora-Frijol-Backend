from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    points = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'user' 

    def __str__(self):
        return self.email