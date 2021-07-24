from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from .serializer import CarSerializer
from core.models import Car
from core.paginations.car_pagination import CarPagination
from django.contrib.auth import get_user_model
from core.filters.car_filter import CarFilter

UserModel = get_user_model()


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    pagination_class = CarPagination
    filterset_class = CarFilter
    queryset = Car.objects.all()



class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarByUserIdListView(ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        qs = Car.objects.all()
        params = self.request.query_params
        user_id = params.get('userId', None)
        if user_id:
            qs = qs.filter(user_id=user_id)
        return qs




