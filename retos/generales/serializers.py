from rest_framework import serializers
from . import models


class TeamSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = models.Team
        fields = ('team_id', 'name', 'longitude', 'latitude', 'status', 'logo')

class CategoryTeamSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = models.CategoryTeam
        fields = ('category_id', 'category', 'team', 'uniform_color', 'status')

class KindOfTeamSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = models.KindOfTeam
        fields = ('kindof_id', 'kindof','team')

class UsersTeamSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = models.UsersTeam
        fields = ('user', 'team', 'date_inserted', 'status')