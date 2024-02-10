from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    music = serializers.ReadOnlyField(source='music.name_music')

    class Meta:
        model = Rating
        fields = '__all__'
