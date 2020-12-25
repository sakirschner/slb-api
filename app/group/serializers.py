from django.contrib.auth import get_user_model

from rest_framework import serializers
from core.models import Group, Reward


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for group objects"""
    students = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=get_user_model().objects.all()
    )
    rewards = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Reward.objects.all()
    )

    class Meta:
        model = Group
        fields = ('id', 'name', 'points', 'students', 'rewards')
        read_only_fields = ('id',)