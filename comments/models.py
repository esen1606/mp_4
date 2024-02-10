from django.db import models
from music.models import Music
from django.conf import settings


class Comment(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments", on_delete=models.CASCADE)
    music = models.ForeignKey(Music, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} ==. {self.music}'
    
