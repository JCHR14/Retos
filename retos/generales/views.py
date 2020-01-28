from rest_framework import viewsets
from . import models
from . import serializers
from .permissions import IsOwner

class TeamViewset(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer
    permission_classes = [IsOwner]

class CategoryTeamViewset(viewsets.ModelViewSet):
    queryset = models.CategoryTeam.objects.all()
    serializer_class = serializers.CategoryTeamSerializer
    permission_classes = [IsOwner]

class KindOfTeamViewset(viewsets.ModelViewSet):
    queryset = models.KindOfTeam.objects.all()
    serializer_class = serializers.KindOfTeamSerializer
    permission_classes = [IsOwner]


class UsersTeamViewset(viewsets.ModelViewSet):
    queryset = models.UsersTeam.objects.all()
    serializer_class = serializers.UsersTeamSerializer
    permission_classes = [IsOwner]