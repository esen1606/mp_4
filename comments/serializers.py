from rest_framework import serializers

from music.models import Music
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_username = serializers.ReadOnlyField(source='owner.username')
    music = serializers.CharField(required=False)

    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['post_title'] = instance.music.name_music
        if instance.music.image_music:
            preview = instance.music.image_music
            representation['post_preview'] = preview.url
        else:
            representation['post_preview'] = None
        return representation


class CommentActionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = '__all__'
        
    def create(self, validated_data):
        music = self.context.get('music')
        music = Music.objects.get(pk=music)
        validated_data['post'] = music
        owner = self.context.get('owner')
        validated_data['owner'] = owner
        return super().create(validated_data)