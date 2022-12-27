from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, max_length=100)

    class Meta:
        model = User
        fields = ['email', 'password']
