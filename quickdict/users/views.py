from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth.models import User
from .serializers import UserProfileSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
# Create your views here.


class UserProfileCreateView(CreateAPIView):
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "details": "User created Successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
