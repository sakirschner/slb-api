from django.contrib.auth import get_user_model

from rest_framework import serializers
from core.models import Achievement, StudentAchievement
from user.serializers import UserSerializer


class AchievementSerializer(serializers.ModelSerializer):
    """Serializer for achievement objects"""

    class Meta:
        model = Achievement
        fields = ('id', 'achievement', 'points', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class StudentAchievementSerializer(serializers.ModelSerializer):
    """Serializer for studentachievement objects"""
    student = UserSerializer(
        many=False,
        read_only=True
    )
    achievement = AchievementSerializer(
        many=False,
        read_only=True
    )

    class Meta:
        model = StudentAchievement
        fields = ('id', 'student', 'achievement', 'notes', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')