from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('app.User.urls')),
    path('cars/', include('app.Car.urls')),
    path('auth/', include('app.auth_.urls'))
]