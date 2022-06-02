from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Note


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class NoteSerializer(serializers.ModelSerializer):  # NoteSerializer / NoteCreateSerializer and NoteUpdateSerializer
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Note
        fields = "__all__"
        read_only_fields = ['author', ]


class QueryParamsSerializer(serializers.Serializer):
    state = serializers.ListField(child=serializers.ChoiceField(choices=Note.STATE), required=False)
    important = serializers.ListField(child=serializers.BooleanField(), required=False)
    public = serializers.ListField(child=serializers.BooleanField(), required=False)
