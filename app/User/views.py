from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .serializers import UserSerializer, UserUpDateSerializer
from ..Car.serializer import CarByUserIdSerializer

UserModel: User = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserUpDateSerializer
    queryset = UserModel.objects.all()


class AddCarByIdUserView(CreateAPIView):
    serializer_class = CarByUserIdSerializer
    queryset = UserModel

    def perform_create(self, serializer):
        serializer.save(user=self.get_object())


