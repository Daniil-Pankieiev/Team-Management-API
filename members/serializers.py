from rest_framework import serializers
from .models import Person
from teams.serializers import TeamSerializer
from teams.models import Team


class PersonReadSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)

    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name", "email", "team"]


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name", "email", "team"]
