from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Profile(models.Model):
    class Meta:
        db_table = 'profile'
        app_label = 'core'
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')