from rest_framework.serializers import ModelSerializer
from core.models import Profile

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'age')
