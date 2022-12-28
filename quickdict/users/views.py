from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth.models import User
from .serializers import UserProfileSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.db import transaction
from django.contrib.auth.hashers import make_password
# Create your views here.


class UserProfileCreateView(CreateAPIView):
    serializer_class = UserProfileSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = request.data
        first_name = data.get('first_name', None)
        last_name = data.get('last_name', None)
        username = data.get('username', None)
        email = data.get('email', None)
        phone_number = data.get('phone_number', None)
        date_of_birth = data.get('date_of_birth', None)
        password = data.get('password', None)

        if User.objects.filter(username=username).exists():
            return Response(data={'details': 'User name already exists. '}, status=status.HTTP_406_NOT_ACCEPTABLE)
        user = User(first_name=first_name, last_name=last_name, username=username, email=email,
                    password=make_password(password))
        user.save()

        user_profile = UserProfile(phone_number=phone_number, date_of_birth=date_of_birth, user=user)
        user_profile.save()
        return Response(data={'details': 'User Created'}, status=status.HTTP_201_CREATED)
