from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class UserProfileSerializer(ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = UserProfile
        exclude = ['user']
