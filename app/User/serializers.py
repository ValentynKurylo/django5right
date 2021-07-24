from rest_framework.serializers import ModelSerializer
from core.models import CustomUser
from app.ProfileUser.serializers import ProfileSerializer
from core.models import Profile
from django.contrib.auth import get_user_model
from app.Car.serializer import CarSerializer

UserModel = get_user_model()

class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'profile', 'cars')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = CustomUser.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile)
        return user


class UserUpDateSerializer(UserSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'profile', 'cars')

    def update(self, instance, validated_data):
        profile = validated_data.pop('profile', None)
        if profile:
            ProfileSerializer().update(instance.profile, profile)
        return super().update(instance, validated_data)

