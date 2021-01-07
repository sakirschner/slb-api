# from django.contrib.auth import get_user_model

from rest_framework import serializers
from core.models import Group
from reward.serializers import RewardSerializer
from user.serializers import UserSerializer


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for group objects"""
    students = UserSerializer(
        many=True,
        read_only=True
    )
    rewards = RewardSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Group
        fields = ('id', 'name', 'points', 'students', 'rewards')
        read_only_fields = ('id',)