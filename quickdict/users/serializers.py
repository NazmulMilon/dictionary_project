from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework.serializers import ModelSerializer


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
