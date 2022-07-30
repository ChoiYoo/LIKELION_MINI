from .models import Movies, Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'Movies', 'user', 'created_at', 'comment']
        read_only_fields = ['id']