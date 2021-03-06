from rest_framework import viewsets, mixins, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import Achievement, StudentAchievement, User
from achievement import serializers

import django_filters

from django_filters import rest_framework as filters

from django_filters.rest_framework import DjangoFilterBackend


class AchievementViewSet(viewsets.GenericViewSet,
                         viewsets.ViewSet,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin):
    """Manage Achievements in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Achievement.objects.all()
    serializer_class = serializers.AchievementSerializer

    def get_queryset(self):
        """Return all objects"""
        return self.queryset

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save()


class GetAchievementByIdView(generics.RetrieveUpdateDestroyAPIView):
    """Lists single achievement from the database by id"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.AchievementSerializer

    def get_object(self, **kwargs):
        """Return object for user"""
        return Achievement.objects.get(id=self.kwargs['pk'])


class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    """will seperate the ids in the url parameters"""
    pass


class StudentAchievementFilter(django_filters.FilterSet):
    """Filters achievements based on user id"""
    # studentachievements = django_filters.MultipleChoiceFilter(
    #     field_name='student__id',
    #     lookup_expr="icontains",
    #     conjoined=True,
    # )

    student_in = NumberInFilter(
        field_name='student__id',
        lookup_expr='in',
        )

    class Meta:
        model = StudentAchievement
        fields = ['student_in',]     


class StudentAchievementViewSet(viewsets.GenericViewSet,
                         viewsets.ViewSet,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin):
    """Manage Achievements in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = StudentAchievement.objects.all()
    serializer_class = serializers.StudentAchievementSerializer
    filter_backends = [DjangoFilterBackend]
    # filter_fields = ('id', 'student')
    filter_class = StudentAchievementFilter

    def get_queryset(self):
        """Return all objects"""
        return self.queryset

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save()


class GetStudentAchievementByIdView(generics.RetrieveUpdateDestroyAPIView):
    """Lists single studentachievement from the database by id"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.StudentAchievementSerializer

    def get_object(self, **kwargs):
        """Return object for user"""
        return StudentAchievement.objects.get(id=self.kwargs['pk'])