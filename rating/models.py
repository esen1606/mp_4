from django.db import models
from django.contrib.auth import get_user_model
from music.models import Music

User = get_user_model()


class Rating(models.Model):
    music = models.ForeignKey(Music, related_name='ratings', on_delete=models.CASCADE)
    value = models.IntegerField(default=0, choices=[(i, str(i)) for i in range(1, 11)])


    def __str__(self):
        return f"{self.music.name_music} - {self.value}"
