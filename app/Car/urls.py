from django.urls import path

from .views import CarListCreateView, CarRetrieveUpdateDestroyView, CarByUserIdListView


urlpatterns = [
    path('', CarListCreateView.as_view(), name='car_list_create'),
    path('user/', CarByUserIdListView.as_view()),
    path('<int:pk>/', CarRetrieveUpdateDestroyView.as_view(), name='car_retrieve_update_destroy'),

]