
from django.urls import path, include

urlpatterns = [

    path('api/', include('api.api_v1'))
]