from rest_framework.serializers import ModelSerializer
from core.models import Car

class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        #fields = '__all__'
        fields = ('id', 'brand', 'year', 'user')
        extra_kwargs = {
            'user': {'write_only': True}
        }


class CarByUserIdSerializer(CarSerializer):
    class Meta:
        model = Car
        fields = ('id', 'brand', 'year')
