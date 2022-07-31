
from rest_framework import serializers
from dataclasses import field
from .models import Movie, Staff, Comment

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
        read_only_fields = ['movie_title']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['id']

class MovieSerializer(serializers.ModelSerializer):
    staffs = StaffSerializer(many=True)
    comments = CommentSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'