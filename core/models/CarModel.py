from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Car(models.Model):
    class Meta:
        db_table = 'cars'
        app_label = 'core'

    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cars')