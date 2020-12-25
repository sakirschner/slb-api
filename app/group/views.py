from rest_framework import viewsets, mixins, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import Group
from group import serializers


class GroupViewSet(viewsets.GenericViewSet,
                         viewsets.ViewSet,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin):
    """Manage Groups in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer

    def get_queryset(self):
        """Return all objects"""
        return self.queryset

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save()


class GetGroupByIdView(generics.RetrieveUpdateDestroyAPIView):
    """Lists single group from the database by id"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.GroupSerializer

    def get_object(self, **kwargs):
        """Return object for user"""
        return Group.objects.get(id=self.kwargs['pk'])
