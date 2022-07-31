
from rest_framework import serializers
from .models import Movie, Staff, Comment

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
        read_only_fields = ['movie_title']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Comment
        fields = ['id', 'movies', 'user', 'created_at', 'comment']

class MovieSerializer(serializers.ModelSerializer):
    staffs = StaffSerializer(many=True)
    comments = CommentSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'