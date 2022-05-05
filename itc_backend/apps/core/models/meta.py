from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class AbstractTimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(to=UserModel, null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True
